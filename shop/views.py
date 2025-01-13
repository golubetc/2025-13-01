from django.shortcuts import render, redirect
from .models import PositionOrders
from .forms import PositionOrdersForm


def orders(request):
    orders = PositionOrders.objects.all()
    return render(request, 'shop/index.html', context={'orders': orders})


def add_orders(request):
    if request.method == 'POST':
        form = PositionOrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        return redirect('add_orders')
    form = PositionOrdersForm()
    return render(request, 'shop/add_orders.html', context={'form': form})
