from django.urls import path

from CW_places.views import CWPlacesView

urlpatterns = [
    path('', CWPlacesView.as_view({'get': 'list'}), name='cw places'),
]