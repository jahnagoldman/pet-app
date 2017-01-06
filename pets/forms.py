from django import forms
from django.forms import DateField
from .models import Pet
from petproject import settings

class PetForm(forms.ModelForm):
    # use settings for date input
    birthday = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Pet
        fields = ('name', 'animal', 'birthday', 'microchip_number' )
