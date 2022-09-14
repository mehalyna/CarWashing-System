"""
Serializer class used with Django rest_framework
"""

from rest_framework import serializers

from order_details.models import OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for OrderDetails model. Use ModelSerializer which is
    a regular Serializer, except that:
        - A set of default fields are automatically populated.
        - A set of default validators are automatically populated.
        - Default '.create()' and '.update()' implementations are provided.
    """
    class Meta:
        """
        Use Meta for setting up the behaviour of OrderDetailSerializer class.
        `fields = '__all__'`, takes all fields from OrderDetails.
        """
        model = OrderDetail
        fields = '__all__'
