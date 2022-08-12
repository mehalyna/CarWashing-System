from rest_framework import viewsets
from places.models import Places
from places.serializers import PlacesSerializer


class PlacesView(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
