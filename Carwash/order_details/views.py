from rest_framework import viewsets
from rest_framework import permissions

from order_details.serializer import OrderDetailSerializer
from order_details.models import OrderDetail


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderDetail to be viewed or edited.
    """
    queryset = OrderDetail.objects.all().order_by('order')
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
