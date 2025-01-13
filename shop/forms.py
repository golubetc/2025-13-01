from .models import PositionOrders
from django import forms


class PositionOrdersForm(forms.ModelForm):
    class Meta:
        model = PositionOrders
        fields = ['position', 'orders']