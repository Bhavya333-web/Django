from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Book
from .forms import ContactForm, ContactModelForm, BookForm
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
