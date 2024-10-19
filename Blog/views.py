from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Add this line
from .models import Employee, Book, Blog  # Add Blog model
from .forms import ContactForm, ContactModelForm, BookForm, BlogForm  # Add BlogForm
from taggit.models import Tag

# Combined Contact Form View
def contact_view(request):
    contact_form = ContactForm()
    model_form = ContactModelForm()
    success_message = ""

    if request.method == 'POST':
        if 'contact_form' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                # Process the data in contact_form.cleaned_data as required
                print(contact_form.cleaned_data)
                success_message = "Contact form submitted successfully!"
        
        elif 'model_form' in request.POST:
            model_form = ContactModelForm(request.POST)
            if model_form.is_valid():
                model_form.save()  # Save the model form data to the database
                success_message = "Your message has been sent successfully!"

    return render(request, 'contact.html', {
        'contact_form': contact_form,
        'model_form': model_form,
        'success_message': success_message,
    })

# App View (For Employee and Book display with Tag filtering)
def app_view(request):
    emp = Employee.objects.all()
    books = Book.objects.all()

    # Filter by tag if provided
    tag_filter = request.GET.get('tag')
    if tag_filter:
        books = books.filter(tags__name__in=[tag_filter])

    tags = Tag.objects.all()  # Get all tags for the dropdown

    return render(request, 'app.html', {
        'emp': emp,
        'books': books,
        'tags': tags,
        'tag_filter': tag_filter,
    })

# Book Creation/Edit View
def book_create_edit(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, id=book_id)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Save the book and its tags
            return redirect('app')  # Redirect to app view after saving
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# About Page View
def about_view(request):
    return render(request, 'about.html')

# Static Contact Page View
def static_contact_view(request):
    return render(request, 'contact_static.html')

# **New Blog Update View with @login_required**
@login_required  # Only logged-in users can update the blog
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  # Get the blog post by its primary key (pk)
    tag_list = list(blog.tags.values_list('name', flat=True))  # Get list of existing tags for the blog

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)  # Populate form with new data
        if form.is_valid():
            form.save()  # Save the updated blog post
            return redirect('home')  # Redirect to home after saving
    else:
        form = BlogForm(instance=blog)  # Pre-fill the form with current blog data
        form.initial['tags'] = ', '.join(tag_list)  # Show current tags as a comma-separated string

    return render(request, 'blog/update_blog.html', {'form': form, 'blog': blog})
