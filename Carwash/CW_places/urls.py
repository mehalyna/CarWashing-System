from django.urls import path, include
from rest_framework import routers

from CW_places.views import CWPlacesView

router = routers.DefaultRouter()
router.register(r'cw_places', CWPlacesView)

urlpatterns = [
    path('', include(router.urls)),
]
