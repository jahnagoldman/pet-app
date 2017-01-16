from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.views.generic import ListView
from .forms import PetForm
from .models import Pet


# Create your views here.

class NewPetView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'pets/new_pet.html'
    form_class = PetForm
    success_url = '/pets/'

    def form_valid(self, form):
        # this method is called when valid form data has been POSTed - returns HTTPResponse
        name = form.cleaned_data['name']
        animal = form.cleaned_data['animal']
        birthday = form.cleaned_data['birthday']
        microchip_number = form.cleaned_data['microchip_number']
        owner = self.request.user
        new_pet = Pet.create(owner, name, animal, birthday, microchip_number)
        return super(NewPetView, self).form_valid(form)


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
