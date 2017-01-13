from django import forms
from django.forms import DateField, DateTimeField, models

from pets.models import Pet
from .models import Walk
from petproject import settings

class WalkForm(forms.ModelForm):
    # use settings for date input
    class Meta:
        model = Walk
        fields = ('pet', 'walk_time', 'walk_date', 'comments')

