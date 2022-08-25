from rest_framework import viewsets, permissions
from places.models import Places
from places.serializers import PlacesSerializer


class PlacesView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
