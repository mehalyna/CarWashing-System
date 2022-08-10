from django.shortcuts import render
from django.views import generic as views

from car_washes.models import CarWashes


class CarWashesListView(views.ListView):
    model = CarWashes
    ordering = ('car_wash_name',)
    context_object_name = 'car_washes'
    template_name = 'car_washes/car_washes_list.html'
