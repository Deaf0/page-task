from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('create', views.create, name='create'),
]