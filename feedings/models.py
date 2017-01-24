from datetime import date

import django
from django import template
from django.db import models

# Create your models here.
from pets.models import Pet

class Event(models.Model):
    pet = models.ForeignKey(Pet(), on_delete=models.CASCADE, default=None)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    comments = models.TextField(blank=True)
    W = 'Walk'
    B = 'Bathroom'
    M = 'Medicine'
    F = 'Feeding'
    EVENT_TYPE_CHOICES = {
        (W, 'Walk'),
        (B, 'Bathroom'),
        (M, 'Medicine'),
        (F, 'Feeding'),
    }
    event_type = models.CharField(max_length=1, choices=EVENT_TYPE_CHOICES)

    class Meta:
        abstract=False

class Feeding(Event):

    def __str__(self):
        return self.time

    @classmethod
    def create(cls, pet, time, date, comments, event_type):
        feeding = cls(pet=pet, time=time, date=date, comments=comments, event_type=event_type)
        feeding.save()
        return feeding
