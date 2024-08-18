from django.shortcuts import render
from django.http import HttpResponse
def style(request):
    return render(request,'app.html')

# Create your views here.
