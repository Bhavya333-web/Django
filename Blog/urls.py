from django.urls import path
from . import views
from .views import delete_book  
from .views import create_blog
from .views import register, home_view

urlpatterns = [

    path('', views.app_view, name="app"), 
    path('home/', home_view, name='home'),  # Home page
    path('about/', views.about_view, name='about'),  # About page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('app/book/new/', views.book_create_edit, name='book_create_edit'),  # URL for creating a new book
    path('app/book/edit/<int:book_id>/', views.book_create_edit, name='book_edit'),  # URL for editing an existing book
    path('edit/<int:pk>/', views.update_blog, name='update_blog'),
    path('create/', create_blog, name='create_blog'),  
    path('delete/<int:book_id>/', delete_book, name='delete'),
    path('register/', register, name='register'),
     path('send-email/', views.send_email_view, name='send_email'),
   
]

