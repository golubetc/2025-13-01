from django.urls import path
from .views import update_recipe, \
    delete_recipe, add_recipe, recipes

urlpatterns = [
    path('main/', recipes, name='main'),
    path('add/', add_recipe, name='add_recipe'),
    path('update/<int:id>', update_recipe, name='update_recipe'),
    path('delete/<int:id>', delete_recipe, name='delete_recipe'),
]