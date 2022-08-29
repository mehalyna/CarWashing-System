"""
Set up entrypoints for order_details app.
Use routers for simply instantiating a Router class, and then registering
all the required ViewSets with that router.
DefaultRouter adds API root view, and adds format suffix patterns to the URLs.
"""

from django.urls import include, path
from rest_framework import routers
from order_details.views import OrderDetailViewSet

router = routers.DefaultRouter()
router.register(r'order_details', OrderDetailViewSet, basename='order_details')


urlpatterns = [
    path('', include(router.urls)),
]
