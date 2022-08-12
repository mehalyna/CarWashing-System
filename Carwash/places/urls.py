from django.urls import path
from places.views import PlacesView

urlpatterns = (
    path('places/', PlacesView.as_view({'get': 'list'}), name='places'),
)
