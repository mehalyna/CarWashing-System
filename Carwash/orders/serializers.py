from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """

    class Meta:
        model = Order
        fields = '__all__'
