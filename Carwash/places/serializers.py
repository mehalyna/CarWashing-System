from rest_framework import serializers
from places.models import Places


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'
