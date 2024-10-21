from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .models import Employee, Book, Blog
from .forms import ContactForm, ContactModelForm, BookForm, BlogForm, UserRegistrationForm  # Add UserRegistrationForm
from taggit.models import Tag
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import EmailForm


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],  # List of recipient emails
                fail_silently=False,
            )
            return render(request, 'email_success.html')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Ensure your form has this field
            user.save()
            login(request, user)
            
            # Sending Welcome Email to New User
            subject = 'Welcome to Our Mblog!'
            message = f'Hi {user.username},\n\nThank you for signing up on our blog platform. We hope you enjoy your stay!\n\nBest regards,\nThe Team'
            recipient_list = [user.email]
            
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            except Exception as e:
                print(f"Failed to send email: {e}")

            return redirect('home')  
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

    # your view logic





def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('app')
    return render(request, 'delete.html', {'book_name': book.book_name})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-view-name')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

# Combined Contact Form View
def contact_view(request):
    contact_form = ContactForm()
    model_form = ContactModelForm()
    success_message = ""

    if request.method == 'POST':
        if 'contact_form' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                print(contact_form.cleaned_data)
                success_message = "Contact form submitted successfully!"
        
        elif 'model_form' in request.POST:
            model_form = ContactModelForm(request.POST)
            if model_form.is_valid():
                model_form.save()
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

    tag_filter = request.GET.get('tag')
    if tag_filter:
        books = books.filter(tags__name__in=[tag_filter])

    tags = Tag.objects.all()
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
            form.save()
            return redirect('app')
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

# User Registration View

# Blog Update View with @login_required
@login_required
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    tag_list = list(blog.tags.values_list('name', flat=True))

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        form.initial['tags'] = ', '.join(tag_list)

    return render(request, 'blog/update_blog.html', {'form': form, 'blog': blog})

# Blog Delete View with @login_required
@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('home')

    return render(request, 'blog/delete_blog.html', {'blog': blog})
