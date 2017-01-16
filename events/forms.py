from urllib import request

from django import forms
from django.forms import DateField, DateTimeField, models

from pets.models import Pet
from .models import Walk
from petproject import settings

class WalkForm(forms.ModelForm):
    class Meta:
        model = Walk
        fields = ('pet', 'walk_time', 'walk_date', 'comments')
    # override constructor to only display pets that belong to the logged in user
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(WalkForm, self).__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(owner=self.request.user)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

