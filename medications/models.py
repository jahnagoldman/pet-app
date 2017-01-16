from django.db import models
from datetime import date

import django
from django.db import models

# Create your models here.

from pets.models import Pet


class Medication(models.Model):
    pet = models.ForeignKey(Pet(), on_delete=models.CASCADE, default=None)
    HW = 'Heartworm'
    FT = 'Flea/Tick'
    BM = 'Behavior-Modifying'
    AB = 'Antibiotic'
    PR = 'Pain Reliever'
    AF = 'Anti-Inflammatory'
    ST = 'Steroids'
    H = 'Hormones'
    CH = 'Chemotherapeutics'
    MEDICATION_TYPE_CHOICES = {
        (HW, 'Heartworm'),
        (FT, 'Flea/Tick'),
        (BM, 'Behavior-Modifying'),
        (AB, 'Antibiotic'),
        (PR, 'Pain Reliever'),
        (AF, 'Anti-Inflammatory'),
        (ST, 'Steroids'),
        (H, 'Hormones'),
        (CH, 'Chemotherapeutics'),
    }
    medication_type = models.CharField(max_length=100, choices=MEDICATION_TYPE_CHOICES, )
    medication_time = models.TimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    medication_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.medication_time

    @classmethod
    def create(cls, pet, medication_type, medication_time, medication_date, comments):
        medication = cls(pet=pet, medication_type=medication_type, medication_time=medication_time, medication_date=medication_date, comments=comments)
        medication.save()
        return medication

