from django.shortcuts import render
from .models import Employee, Book
from .forms import ContactForm, ContactModelForm

# Combined Contact Form View
def contact_view(request):
    # Initialize both forms
    contact_form = ContactForm()
    model_form = ContactModelForm()
    success_message = ""

    if request.method == 'POST':
        # Check which form was submitted
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

    # Render the template with the forms and success message
    return render(request, 'contact.html', {
        'contact_form': contact_form,
        'model_form': model_form,
        'success_message': success_message,
    })

# App View (For Employee and Book display)
def app_view(request):
    emp = Employee.objects.all()
    books = Book.objects.all()
    return render(request, 'app.html', {'emp': emp, 'books': books})

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# About Page View
def about_view(request):
    return render(request, 'about.html')

# Static Contact Page View
def static_contact_view(request):
    return render(request, 'contact_static.html')
