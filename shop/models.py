from django.db import models


class Orders(models.Model):
    name = models.CharField(max_length=20)


class PositionOrders(models.Model):
    position = models.BooleanField(default=False)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
