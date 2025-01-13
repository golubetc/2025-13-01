from django.urls import path
from .views import get_recipes, update_recipe, delete_recipe, create_recipe

urlpatterns = [
    path('main', get_recipes, name='recipe_get'),
    path('update/<int:id>', update_recipe, name='upadate_recipe'),
    path('delete/<int:id>', delete_recipe, name='delete-recipe'),
    path('create', create_recipe, name='create-recipe')
]