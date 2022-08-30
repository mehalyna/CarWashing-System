from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer
from users.serializers import UsersSerializer


class OrderView(ModelViewSet):
    """
    Order model view set

    Attributes
        queryset: collection of all Order objects/rows in database
        serializer_class: reference to OrderSerializer
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
