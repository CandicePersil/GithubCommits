"""qwarrysiteproject URL Configuration

The `urlpatterns` list routes URLs to views.
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path
from . import views

app_name = 'githubcommits'
urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process, name='process'),
]