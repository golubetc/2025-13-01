from django.shortcuts import render, redirect

from .forms import RecipeForm
from .models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/index.html', context={'recipes': recipes})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        return redirect('add_recipe')
    form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', context={'form': form})


def update_recipe(request, id):
    book = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            book.name = form.cleaned_data['name']
            book.instructions = form.cleaned_data['instructions']
            book.ingredient.name = form.cleaned_data['ingredient']
            book.save()
            return redirect('main')
    form = RecipeForm()
    return render(request, 'recipe/update_recipe.html', context={'form': form})


def delete_recipe(request, id):
    book = Recipe.objects.get(id=id)
    book.delete()
    return redirect('main')
