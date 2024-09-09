from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Book

def app(request):
    emp = Employee.objects.all()
    books = Book.objects.all()
    return render(request, 'app.html', {'emp': emp, 'books': books})

# Remove the style view or modify it to serve an actual HTML template if needed
def style(request):
    # This should render an HTML template, not a CSS file
    return render(request, 'app.html')  # Replace 'your_template.html' with the correct HTML template file

