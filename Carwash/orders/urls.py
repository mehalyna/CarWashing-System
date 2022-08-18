from django.urls import path, include
from rest_framework import routers

from orders.views import OrderView


router = routers.DefaultRouter()
router.register(r'orders', OrderView)

urlpatterns = (
    path('', include(router.urls)),
)
