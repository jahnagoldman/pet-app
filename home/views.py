from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Model
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from bathroom.models import Bathroom
from feedings.models import Feeding
from medications.models import Medication
from walks.models import Walk


class LogInHomeView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'home/login_home_page.html'
    model = Walk

    def get_context_data(self, **kwargs):
        context = super(LogInHomeView, self).get_context_data(**kwargs)
        context['feeding_list'] = Feeding.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')[:3]
        context['bathroom_list'] = Bathroom.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')[:3]
        context['medication_list'] = Medication.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')[:3]
        return context

    def get_queryset(self):
        return Walk.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')[:3]

class HomeView(TemplateView):
    template_name = 'home/home_page.html'
