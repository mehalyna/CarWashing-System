from rest_framework import generics as api_views

from car_washes.models import CarWashes
from car_washes.serializers import CarWashesSerializer



class CarWashesCreate(api_views.ListCreateAPIView):
    queryset = CarWashes.objects.all()
    serializer_class = CarWashesSerializer
    permission_classes = ()

