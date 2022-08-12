from django.urls import path, include
from rest_framework import routers
from places.views import PlacesView


router = routers.DefaultRouter()
router.register(r'places', PlacesView)

urlpatterns = (
    path('', include(router.urls)),
)
