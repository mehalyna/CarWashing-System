from rest_framework import serializers
from carwash_services.models import Carwash_Services, Services


class CarWashServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carwash_Services
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

