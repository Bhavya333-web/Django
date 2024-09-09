from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.app, name="app"),
]
