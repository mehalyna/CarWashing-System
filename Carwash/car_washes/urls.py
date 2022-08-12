from django.urls import path, include

from rest_framework import routers

from car_washes.views import CarWashSet

router = routers.DefaultRouter()
router.register(r'car_washes', CarWashSet)
urlpatterns = (
    path('', include(router.urls)),
)
