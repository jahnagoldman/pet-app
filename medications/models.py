from datetime import date
import django
from django import template
from django.db import models

from feedings.models import Event
from pets.models import Pet


# Create your models here.


class Medication(Event):
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

    def __str__(self):
        return self.time

    @classmethod
    def create(cls, pet, medication_type, time, date, comments, event_type):
        medication = cls(pet=pet, medication_type=medication_type, time=time,
                         date=date, comments=comments, event_type=event_type)
        medication.save()
        return medication

