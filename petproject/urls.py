"""dogproject URL Configuration

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
from accounts.views import (login_view, register_view, logout_view,)
from pets.views import create_pet_view, PetListView
from events.views import index
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^pets/$', PetListView.as_view(), name='pet-list'),
    url(r'^pets/new/$', create_pet_view, name='new_pet'),
    url(r'^', index, name='home'),

]
