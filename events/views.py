from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event, Register_data


def books(request):
    books = Register_data.objects.all()
    return render(request, 'events/index.html', context={'books': books})


def add_book(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        return redirect('add_book')
    form = EventForm()
    return render(request, 'events/add_events.html', context={'form': form})


def update_book(request, id):
    event = Register_data.objects.get(id=id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event.attendee = form.cleaned_data['attendee']
            event.event = form.cleaned_data['event']
            event.save()
            return redirect('main')
        return redirect('add_book')
    form = EventForm()
    return render(request, 'events/update_events.html', context={'form': form})


def delete_book(request, id):
    book = Event.objects.get(id=id)
    book.delete()
    return redirect('main')
