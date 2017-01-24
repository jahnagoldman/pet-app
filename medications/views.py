from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic import ListView
from medications.forms import MedicationForm
from medications.models import Medication


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'base.html')


class NewMedicationView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'medications/new_medication.html'
    form_class = MedicationForm
    success_url = '/medications/'

    # make request available as one of keyword arguments to the medicationForm's init constructor method
    def get_form_kwargs(self):
        kw = super(NewMedicationView, self).get_form_kwargs()
        kw['request'] = self.request  # the trick!
        return kw

    def form_valid(self, form):
        # this method is called when valid form data has been POSTed - returns HTTPResponse
        pet = form.cleaned_data['pet']
        medication_type = form.cleaned_data['medication_type']
        time = form.cleaned_data['time']
        date = form.cleaned_data['date']
        comments = form.cleaned_data['comments']
        new_medication = Medication.create(pet, medication_type, time, date, comments)
        return super(NewMedicationView, self).form_valid(form)


# login required for a class
class MedicationListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Medication
    template_name = 'medications/medication_list.html'

    def get_queryset(self):
        return Medication.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')

    def get_context_data(self, **kwargs):
        context = super(MedicationListView, self).get_context_data(**kwargs)
        context['medication_list'] = Medication.objects.all()
        return context
