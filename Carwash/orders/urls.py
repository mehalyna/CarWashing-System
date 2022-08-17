from django.urls import path

from orders.views import OrderView


urlpatterns = (
    path('orders/', OrderView.as_view(), name='orders'),
    path('orders/<int:pk>', OrderView.as_view(), name='order')
)
