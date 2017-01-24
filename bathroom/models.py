from django.db import models
from datetime import date
import django
from django.db import models
from pets.models import Pet


# Create your models here.


class Bathroom(models.Model):
    pet = models.ForeignKey(Pet(), on_delete=models.CASCADE, default=None)
    PEE = 'Pee'
    POOP = 'Poop'
    BATHROOM_TYPE_CHOICES = {
        (PEE, 'Pee'),
        (POOP, 'Poop'),
    }
    bathroom_type = models.CharField(max_length=4, choices=BATHROOM_TYPE_CHOICES, )
    time = models.TimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.time

    @classmethod
    def create(cls, pet, bathroom_type, time, date, comments):
        bathroom = cls(pet=pet, bathroom_type=bathroom_type, time=time, date=date,
                       comments=comments)
        bathroom.save()
        return bathroom
