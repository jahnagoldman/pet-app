from django.db import models
from pets.models import Pet

# Create your models here.
# MVC model view controller

class Walk(models.Model):
    walk_id = models.PositiveIntegerField(primary_key=True)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    comments = models.TextField()

    def __str__(self):
        return self.walk_id
