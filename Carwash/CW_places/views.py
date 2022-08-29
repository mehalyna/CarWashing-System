from rest_framework import viewsets, permissions
from CW_places.serializers import CWPlacesSerializer
from CW_places.models import CWPlaces


class CWPlacesView(viewsets.ModelViewSet):

    """Python function that takes http requests and returns http response."""
    queryset = CWPlaces.objects.all()
    serializer_class = CWPlacesSerializer
