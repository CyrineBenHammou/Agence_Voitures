from django.urls import path
from . import views

urlpatterns = [
    path('App/', views.App, name='App'),
]