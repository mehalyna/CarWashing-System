from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
