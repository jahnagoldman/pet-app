from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic import ListView
from walks.forms import WalkForm
from walks.models import Walk


# Create your views here.

# @login_required(login_url='/login/')
# def index(request):
#     return render(request, 'base.html')


class NewWalkView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'walks/new_walk.html'
    form_class = WalkForm
    success_url = '/walks/'

    # make request available as one of keyword arguments to the WalkForm's init constructor method
    def get_form_kwargs(self):
        kw = super(NewWalkView, self).get_form_kwargs()
        kw['request'] = self.request  # the trick!
        return kw

    def form_valid(self, form):
        # this method is called when valid form data has been POSTed - returns HTTPResponse
        pet = form.cleaned_data['pet']
        time = form.cleaned_data['time']
        date = form.cleaned_data['date']
        comments = form.cleaned_data['comments']
        event_type = 'W'
        new_walk = Walk.create(pet, time, date, comments, event_type)
        return super(NewWalkView, self).form_valid(form)


# login required for a class
class WalkListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Walk
    template_name = 'walks/walk_list.html'

    def get_queryset(self):
        return Walk.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')

    def get_context_data(self, **kwargs):
        context = super(WalkListView, self).get_context_data(**kwargs)
        context['walk_list'] = Walk.objects.all()
        context['model'] = self.model
        return context
