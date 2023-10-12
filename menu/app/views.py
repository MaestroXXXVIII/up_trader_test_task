from django.shortcuts import render
from django.urls import resolve

from .models import MenuItem


def menu_view(request, title):
    current_path_name = f'{request.scheme}://{request.get_host()}'
    return render(request, 'app/index.html', {'title': title,
                                              'path': current_path_name})
