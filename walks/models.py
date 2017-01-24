from datetime import date
import django
from pets.models import Pet
from django.db import models


# Create your models here.
# MVC model view controller

class Walk(models.Model):
    pet = models.ForeignKey(Pet(), on_delete=models.CASCADE, default=None)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.time

    @classmethod
    def create(cls, pet, time, date, comments):
        walk = cls(pet=pet, time=time, date=date, comments=comments)
        walk.save()
        return walk
