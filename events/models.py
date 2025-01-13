from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Участник {self.name}'


class Event(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    attendee = models.ManyToManyField(Attendee, through='Register_data')

    def __str__(self):
        return f'событие {self.name}, создано: {self.date} и будет выполняться участником {self.attendee.name}'


class Register_data(models.Model):
    register_data = models.DateField(auto_now=True)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)



