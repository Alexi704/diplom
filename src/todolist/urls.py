"""todolist URL Configuration"""
from django.contrib import admin
from django.urls import path

from todolist.view import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', health_check, name='health-check'),
]
