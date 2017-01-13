from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
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
        return redirect("/pets/")
    return render(request, 'events/new_walk.html', {'form': form})
