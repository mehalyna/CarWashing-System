from CW_places.models import CWPlaces
from rest_framework import serializers


class CWPlacesSerializer(serializers.ModelSerializer):

    """Responsible for converting objects into data types"""
    class Meta:
        model = CWPlaces
        fields = '__all__'
