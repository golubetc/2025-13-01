from django.shortcuts import render, redirect
from .models import Book
from .forms import AddBookForm


def books(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', context={'books': books})


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        return redirect('add_book')
    form = AddBookForm()
    return render(request, 'library/add_book.html', context={'form': form})


def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book.author.name = form.cleaned_data['author']
            book.title = form.cleaned_data['title']
            book.genre.name = form.cleaned_data['genre']
            book.save()
            return redirect('main')
        return redirect('add_book')
    form = AddBookForm()
    return render(request, 'library/update_book.html', context={'form': form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('main')

