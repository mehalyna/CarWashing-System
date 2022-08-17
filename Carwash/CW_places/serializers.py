from CW_places.models import CWPlaces
from rest_framework import serializers


class CWPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CWPlaces
        fields = '__all__'
