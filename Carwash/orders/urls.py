from django.urls import path

from orders.views import OrderView


urlpatterns = (
    path('orders/', OrderView.as_view({'get': 'list'}), name='orders'),
)
