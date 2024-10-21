
from django.contrib import admin
from django.urls import path,include
from Blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
]

