"""
View for order_details app set as ModelViewSet.
"""

from rest_framework import viewsets
from rest_framework import permissions

from order_details.serializer import OrderDetailSerializer
from order_details.models import OrderDetail


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderDetail to be viewed or edited.
    With 'queryset' the order is set to depends on "order" field in OrderDetails.
    With 'permission_classes', access is allowed to authenticated users.
    """

    queryset = OrderDetail.objects.all().order_by('order')
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
