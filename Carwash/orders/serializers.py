from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance.
        Check the request method and set the depth of related tables for JSON response.
        """

        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2
            self.Meta.read_only_fields = ('car_wash', 'user')

    class Meta:
        model = Order
        fields = '__all__'
