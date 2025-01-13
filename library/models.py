from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=20)
    publication_date = models.DateField(auto_now=True)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)
