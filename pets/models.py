from django.db import models

# Create your models here.


class Pet(models.Model):
    pet_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    DOG = "Dog"
    CAT = "Cat"
    ANIMAL_CHOICES = {
        ('dog', 'DOG'),
        ('cat', 'CAT'),
    }
    animal = models.CharField(max_length=3, choices=ANIMAL_CHOICES,default=DOG)
    birthday = models.DateField
    microchip_number = models.CharField(max_length=30)
