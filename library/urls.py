from django.urls import path
from .views import books, add_book, update_book, delete_book

urlpatterns = [
    path('main/', books, name='main'),
    path('add/', add_book, name='add_book'),
    path('update/<int:id>', update_book, name='update_book'),
    path('delete/<int:id>', delete_book, name='delete_book'),
]