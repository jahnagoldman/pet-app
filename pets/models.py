from django.db import models

# Create your models here.


class Pet(models.Model):
    pet_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    DOG = 'D'
    CAT = 'C'
    ANIMAL_CHOICES = {
        (DOG, 'Dog'),
        (CAT, 'Cat'),
    }
    animal = models.CharField(max_length=3, choices=ANIMAL_CHOICES,)
    birthday = models.DateField(auto_now = False, auto_now_add=False)
    # microchip is an optional field
    microchip_number = models.CharField(max_length=30, blank=True)

    @classmethod
    def create(cls, name, animal, birthday, microchip_number):
        pet = cls(name=name, animal=animal, birthday=birthday, microchip_number=microchip_number)
        return pet

