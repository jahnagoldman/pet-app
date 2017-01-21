from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import TemplateView

from bathroom.models import Bathroom
from feedings.models import Feeding
from medications.models import Medication
from pets.models import Pet
from walks.models import Walk


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'home/home_page.html'


    # def get_queryset(self):
    #     return Pet.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['feeding_list'] = Feeding.objects.filter(pet__owner=self.request.user, ).order_by('-feeding_date', '-feeding_time')[:3]
        context['bathroom_list'] = Bathroom.objects.filter(pet__owner=self.request.user).order_by('-bathroom_date', '-bathroom_time')[:3]
        context['walk_list'] = Walk.objects.filter(pet__owner=self.request.user).order_by('-walk_date', '-walk_time')[:3]
        context['medication_list'] = Medication.objects.filter(pet__owner=self.request.user).order_by('-medication_date', '-medication_time')[:3]
        return context