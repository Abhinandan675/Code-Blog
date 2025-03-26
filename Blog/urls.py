from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.bloghome, name='blog'),
    path('blog/<str:slug>', views.blogpost, name='blogpost'),
    
]