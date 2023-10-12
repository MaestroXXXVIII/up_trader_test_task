from django.shortcuts import render
from django.urls import resolve

from .models import MenuItem


def menu_view(request, title):
    return render(request, 'app/index.html', {'title': title, })
