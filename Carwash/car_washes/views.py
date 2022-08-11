from rest_framework import viewsets

from car_washes.models import CarWashes
from car_washes.serializers import CarWashesSerializer


class CarWashSet(viewsets.ModelViewSet):
    queryset = CarWashes.objects.all()
    serializer_class = CarWashesSerializer
