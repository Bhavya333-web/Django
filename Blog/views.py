from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Book

def app(request):
    emp = Employee.objects.all()
    books = Book.objects.all()
    return render(request, 'app.html', {'emp': emp, 'books': books})

def home_view(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")

def about_view(request):
    return HttpResponse("<h1>About Us Page</h1>")

def contact_view(request):
    return HttpResponse("<h1>Contact Us Page</h1>")