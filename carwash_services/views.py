from django.shortcuts import render
from rest_framework import viewsets

from carwash_services.models import Services, Carwash_Services
from carwash_services.serializers import ServicesSerializer, CarWashServicesSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class CarwashServicesView(viewsets.ModelViewSet):
    queryset = Carwash_Services.objects.all()
    serializer_class = CarWashServicesSerializer
