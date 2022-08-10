from rest_framework import viewsets, permissions
from CW_places.serializers import CWPlacesSerializer
from CW_places.models import CWPlaces


class CWPlacesView(viewsets.ModelViewSet):
    queryset = CWPlaces.objects.all()
    serializer_class = CWPlacesSerializer
    permission = ()
