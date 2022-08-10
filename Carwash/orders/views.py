from rest_framework import viewsets

from orders.models import Order
from orders.serializers import OrderSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
