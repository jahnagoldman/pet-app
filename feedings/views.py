from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic import ListView

from feedings.forms import FeedingForm
from feedings.models import Feeding


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'base.html')


class NewFeedingView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'feedings/new_feeding.html'
    form_class = FeedingForm
    success_url = '/feedings/'

    # make request available as one of keyword arguments to the FeedingForm's init constructor method
    def get_form_kwargs(self):
        kw = super(NewFeedingView, self).get_form_kwargs()
        kw['request'] = self.request  # the trick!
        return kw

    def form_valid(self, form):
    # this method is called when valid form data has been POSTed - returns HTTPResponse
        pet = form.cleaned_data['pet']
        feeding_time = form.cleaned_data['feeding_time']
        feeding_date = form.cleaned_data['feeding_date']
        comments = form.cleaned_data['comments']
        new_feeding = Feeding.create(pet, feeding_time, feeding_date, comments)
        return super(NewFeedingView, self).form_valid(form)

# login required for a class
class FeedingListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Feeding
    template_name = 'feedings/feeding_list.html'

    def get_queryset(self):
        return Feeding.objects.filter(pet__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(FeedingListView, self).get_context_data(**kwargs)
        context['feeding_list'] = Feeding.objects.all()
        return context