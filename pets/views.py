
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from .forms import PetForm
from .models import Pet
# Create your views here.


@login_required(login_url='/login/')
def create_pet_view(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        animal = form.cleaned_data['animal']
        birthday = form.cleaned_data['birthday']
        microchip_number = form.cleaned_data['microchip_number']
        owner = request.user
        new_pet = Pet.create(owner, name, animal, birthday, microchip_number)
        new_pet.save()
        print(new_pet.name)
        return redirect("/pets/")
    return render(request, 'pets/new_pet.html', {'form': form})

class PetListView(ListView):
    model = Pet
    def get_context_data(self, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# @login_required(login_url='/login/')
# def all_pets_view(request):


