from datetime import date
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.http import request
from django.template.backends import django

from petproject import settings


class Pet(models.Model):
    pet_id = models.PositiveIntegerField(primary_key=True, default=0)
    owner = models.ForeignKey(User(), on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30)
    DOG = 'D'
    CAT = 'C'
    ANIMAL_CHOICES = {
        (DOG, 'Dog'),
        (CAT, 'Cat'),
    }
    animal = models.CharField(max_length=3, choices=ANIMAL_CHOICES,)
    birthday = models.DateField(auto_now = False, auto_now_add=False, default=date.today)
    # microchip is an optional field
    microchip_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
    @classmethod
    def create(cls, owner, name, animal, birthday, microchip_number):
        pet = cls(owner=owner, name=name, animal=animal, birthday=birthday, microchip_number=microchip_number)
        return pet

