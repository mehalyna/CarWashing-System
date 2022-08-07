from django.urls import include, path
from rest_framework import routers
from order_details.views import OrderDetailViewSet

router = routers.DefaultRouter()
router.register(r'order_details', OrderDetailViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
