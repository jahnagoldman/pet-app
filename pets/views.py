from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet
# Create your views here.



def create_pet_view(request):
    form = PetForm()
    return render(request, 'pets/new_pet.html', {'form': form})
    # title = "Create A Pet"
    # form = PetForm(request.POST or None)
    # if form.is_valid():
    #     name = form.cleaned_data.get("name")
    #     animal = form.cleaned_data.get("animal")
    #     birthday = form.cleaned_data.get("birthday")
    #     microchip_number = form.cleaned_data.get("microchip_number")
    #     new_pet = Pet.create(name, animal, birthday, microchip_number)
    #     new_pet.save()
    #     # return redirect("/")
    # return render(request, "form.html", {"form": form, "title": title})

