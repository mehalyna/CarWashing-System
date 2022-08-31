from rest_framework import serializers

from car_washes.serializers import CarWashesSerializer
from orders.models import Order
from users.serializers import UsersSerializer

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """

    user_serializer = UsersSerializer(read_only=True, source='user')
    car_wash_serializer = CarWashesSerializer(read_only=True, source='car_wash')

    class Meta:
        model = Order
        fields ='__all__'
