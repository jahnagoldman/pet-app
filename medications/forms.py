from django import forms
from pets.models import Pet
from .models import Medication


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ('pet', 'medication_type', 'medication_time', 'medication_date', 'comments')

    # override constructor to only display pets that belong to the logged in user
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(MedicationForm, self).__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
