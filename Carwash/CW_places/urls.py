from django.urls import path, include
from rest_framework import routers

from CW_places.views import CWPlacesView

router = routers.DefaultRouter()
router.register(r'cw_places', CWPlacesView)

"""Define the mapping between URLs and views. """
urlpatterns = [
    path('api/', include(router.urls)),
]
