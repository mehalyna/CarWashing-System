from rest_framework import serializers

from car_washes.models import CarWashes


class CarWashesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWashes
        fields = '__all__'
