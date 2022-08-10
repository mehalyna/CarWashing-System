from django.urls import include, path
from rest_framework import routers
from order_details.views import OrderDetailViewSet

router = routers.DefaultRouter()
router.register(r'order_details', OrderDetailViewSet, basename='order_details')


urlpatterns = [
    path('', include(router.urls)),
]
