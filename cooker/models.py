from django.db import models



class Cooker(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    text = models.CharField(max_length=150)
    cooker = models.ForeignKey(Cooker, on_delete=models.SET_NULL, null=True)

