from .models import Book
from django import forms


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'author']