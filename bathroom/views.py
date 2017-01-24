from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic import ListView
from bathroom.forms import BathroomForm
from bathroom.models import Bathroom


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'base.html')


class NewBathroomView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'bathroom/new_bathroom.html'
    form_class = BathroomForm
    success_url = '/bathroom/'

    # make request available as one of keyword arguments to the bathroomForm's init constructor method
    def get_form_kwargs(self):
        kw = super(NewBathroomView, self).get_form_kwargs()
        kw['request'] = self.request  # the trick!
        return kw

    def form_valid(self, form):
        # this method is called when valid form data has been POSTed - returns HTTPResponse
        pet = form.cleaned_data['pet']
        bathroom_type = form.cleaned_data['bathroom_type']
        time = form.cleaned_data['time']
        date = form.cleaned_data['date']
        comments = form.cleaned_data['comments']
        new_bathroom = Bathroom.create(pet, bathroom_type, time, date, comments)
        return super(NewBathroomView, self).form_valid(form)


# login required for a class
class BathroomListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Bathroom
    template_name = 'bathroom/bathroom_list.html'

    def get_queryset(self):
        return Bathroom.objects.filter(pet__owner=self.request.user).order_by('-date', '-time')

    def get_context_data(self, **kwargs):
        context = super(BathroomListView, self).get_context_data(**kwargs)
        context['bathroom_list'] = Bathroom.objects.all()
        return context
