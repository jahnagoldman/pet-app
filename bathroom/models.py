from django import template
from django.db import models
from datetime import date
import django
from django.db import models

from feedings.models import Event
from pets.models import Pet


# Create your models here.


class Bathroom(Event):
    PEE = 'Pee'
    POOP = 'Poop'
    BATHROOM_TYPE_CHOICES = {
        (PEE, 'Pee'),
        (POOP, 'Poop'),
    }
    bathroom_type = models.CharField(max_length=4, choices=BATHROOM_TYPE_CHOICES, )

    def __str__(self):
        return self.time

    @classmethod
    def create(cls, pet, bathroom_type, time, date, comments, event_type):
        bathroom = cls(pet=pet, bathroom_type=bathroom_type, time=time, date=date,
                       comments=comments, event_type=event_type)
        bathroom.save()
        return bathroom

