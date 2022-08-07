from Carwash.CW_places.models import CWPlaces
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CWPlaces
        fields = ['carwash_place_id', 'is_free']