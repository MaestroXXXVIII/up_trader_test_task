from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.menu_view, {'title': 'Главная'}, name='main'),
    path('information/', views.menu_view,
         {'title': 'Информация'},
         name='information'),
    path('information/about/', views.menu_view,
         {'title': 'О нас'},
         name='information_about'),
    path('information/contacts/',
         views.menu_view,
         {'title': 'Контакты'},
         name='information_contacts'),
    path('information/price/',
         views.menu_view, {'title': 'Цены'},
         name='information_price'),
]
