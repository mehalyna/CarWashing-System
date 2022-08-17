from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from orders.models import Order
from orders.serializers import OrderSerializer

class OrderView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({
                'error': 'Object Does Not Exist'}
            )
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
