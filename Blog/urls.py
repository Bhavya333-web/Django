from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_view, name="app"),  # Main app view
    path('home/', views.home_view, name='home'),  # Home page
    path('about/', views.about_view, name='about'),  # About page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('app/book/new/', views.book_create_edit, name='book_create_edit'),  # URL for creating a new book
    path('app/book/edit/<int:book_id>/', views.book_create_edit, name='book_edit'),  # URL for editing an existing book
]
