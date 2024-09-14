from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.app, name="app"),
    path('about/', views.about_view, name='about'), 
    path('contact/', views.contact_view, name='contact'),
       
]



            
    