from rest_framework import viewsets, permissions

from car_washes.models import CarWashes
from car_washes.serializers import CarWashesSerializer


class CarWashSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CarWashes.objects.all()
    serializer_class = CarWashesSerializer
