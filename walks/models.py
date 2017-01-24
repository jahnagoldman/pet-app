from datetime import date
import django
from django import template

from feedings.models import Event
from pets.models import Pet
from django.db import models


# Create your models here.
# MVC model view controller

class Walk(Event):

    def __str__(self):
        return self.time

    @classmethod
    def create(cls, pet, time, date, comments, event_type):
        walk = cls(pet=pet, time=time, date=date, comments=comments, event_type=event_type)
        walk.save()
        return walk


