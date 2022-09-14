from rest_framework import serializers

from car_washes.models import CarWashes


class CarWashesSerializer(serializers.ModelSerializer):
    """
    Car Wash Serializer - ModelSerializer for the Car Wash Model with all the fields
    """
    class Meta:
        model = CarWashes
        fields = '__all__'
