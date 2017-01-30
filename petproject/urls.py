"""petproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from accounts.views import (login_view, register_view, logout_view, )
from bathroom.views import BathroomListView, NewBathroomView
from feedings.views import FeedingListView, NewFeedingView
from home.views import LogInHomeView, HomeView, AboutView
from medications.views import MedicationListView, NewMedicationView
from pets.views import PetListView, NewPetView
from walks.views import WalkListView, NewWalkView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^pets/$', PetListView.as_view(), name='pet-list'),
    url(r'^pets/new/$', NewPetView.as_view(), name='new_pet'),
    url(r'^walks/$', WalkListView.as_view(), name='walk-list'),
    url(r'^walks/new/$', NewWalkView.as_view(), name='new_walk'),
    url(r'^feedings/$', FeedingListView.as_view(), name='feeding-list'),
    url(r'^feedings/new/$', NewFeedingView.as_view(), name='new_feeding'),
    url(r'^bathroom/$', BathroomListView.as_view(), name='bathroom-list'),
    url(r'^bathroom/new/$', NewBathroomView.as_view(), name='new_bathroom'),
    url(r'^medications/$', MedicationListView.as_view(), name='medication-list'),
    url(r'^medications/new/$', NewMedicationView.as_view(), name='new_medication'),
    url(r'^home/$', LogInHomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^', HomeView.as_view(), name='home'),

]
