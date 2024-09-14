from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Book

def app(request):
    emp = Employee.objects.all()
    books = Book.objects.all()
    return render(request, 'app.html', {'emp': emp, 'books': books})

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Home Page")

def about_view(request):
    return HttpResponse("This is the About Page")

def contact_view(request):
    return HttpResponse("Contact Us at contact@example.com")




