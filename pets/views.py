from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import FormView
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
        print(new_pet.name)
        return redirect("/pets/")
    return render(request, 'pets/new_pet.html', {'form': form})


# login required for a class
class PetListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Pet
    template_name = 'pets/pet_list.html'

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        context['pet_list'] = Pet.objects.all()
        return context
