from django import forms
from pets.models import Pet
from .models import Walk


class WalkForm(forms.ModelForm):
    class Meta:
        model = Walk
        fields = ('pet', 'time', 'date', 'comments')

    # override constructor to only display pets that belong to the logged in user
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(WalkForm, self).__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
