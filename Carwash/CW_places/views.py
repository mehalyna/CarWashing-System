from django.shortcuts import render
from django.views import generic as views

from Carwash.CW_places.models import CWPlaces


class CWPlacesView(views.ListView):
    model = CWPlaces
    context_object_name = 'cw_places'
    template_name = 'cw_places.html'
