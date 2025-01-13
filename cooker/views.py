from django.shortcuts import render, redirect
from .models import Cooker, Recipe
from .forms import RecipeForm

def get_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'cooker/index.html', context={'recipes': recipes})

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='recipe_get')

    form = RecipeForm
    return render(request, 'cooker/create.html', context={'form': form})


def update_recipe(request, id):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe.objects.get(id=id)
            recipe.text = form.cleaned_data['text']
            recipe.cooker = form.cleaned_data['cooker']
            recipe.save()
            return redirect(to='recipe_get')

    form = RecipeForm
    return render(request, 'cooker/create.html', context={'form': form})


def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect(to='recipe_get')