from django.contrib import admin

from .models import Event, Attendee, Register_data

admin.site.register(Attendee)
admin.site.register(Register_data)
admin.site.register(Event)

