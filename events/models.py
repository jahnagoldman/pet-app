from datetime import date
from django.db import models
from pets.models import Pet


# Create your models here.
# MVC model view controller

class Walk(models.Model):
    pet = models.ForeignKey(Pet(), on_delete=models.CASCADE, default=None)
    walk_time = models.TimeField(auto_now=False, auto_now_add=False)
    walk_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.walk_time

    @classmethod
    def create(cls, pet, walk_time, walk_date, comments):
        walk = cls(pet=pet, walk_time=walk_time, walk_date=walk_date, comments=comments)
        walk.save()
        return walk
