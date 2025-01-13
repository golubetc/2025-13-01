from django.urls import path

from .views import orders, add_orders

urlpatterns = [
    path('main/', orders, name='main'),
    path('add/', add_orders, name='add_book'),
]