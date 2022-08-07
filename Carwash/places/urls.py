from django.urls import path
from places.views import place_name_view

urlpatterns = (
    path('places/', place_name_view, name='places')
)
