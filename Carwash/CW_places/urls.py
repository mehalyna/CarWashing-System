from django.urls import path

from Carwash.CW_places.views import CWPlacesView

urlpatterns = [
    path('cw_places/', CWPlacesView.as_view(), name='cw_places'),
]