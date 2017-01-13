from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView
from events.forms import WalkForm
from events.models import Walk


@login_required(login_url='/login/')
def index(request):
    return render(request, 'base.html')

@login_required(login_url='/login/')
def new_walk_view(request):
    form = WalkForm(request.POST or None)
    if form.is_valid():
        pet = form.cleaned_data['pet']
        walk_time = form.cleaned_data['walk_time']
        walk_date = form.cleaned_data['walk_date']
        comments = form.cleaned_data['comments']
        new_walk = Walk.create(pet, walk_time, walk_date, comments)
        return redirect("/events/walks/")
    return render(request, 'events/new_walk.html', {'form': form})

# login required for a class
class WalkListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Walk
    template_name = 'events/walk_list.html'

    def get_queryset(self):
        return Walk.objects.filter(pet__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(WalkListView, self).get_context_data(**kwargs)
        context['walk_list'] = Walk.objects.all()
        return context