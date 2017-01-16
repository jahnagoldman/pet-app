from datetime import date

import django
from django.db import models

# Create your models here.

from pets.models import Pet


class Feeding(models.Model):
    pet = models.ForeignKey(Pet(), on_delete=models.CASCADE, default=None)
    feeding_time = models.TimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    feeding_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.feed_time

    @classmethod
    def create(cls, pet, feeding_time, feeding_date, comments):
        feeding = cls(pet=pet, feeding_time=feeding_time, feeding_date=feeding_date, comments=comments)
        feeding.save()
        return feeding
