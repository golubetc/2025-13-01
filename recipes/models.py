from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=20)


class Recipe(models.Model):
    name = models.CharField(max_length=20)
    instructions = models.CharField(max_length=50)
    ingredient = models.ManyToManyField(Ingredient)
