from django.urls import path

from car_washes.api_views import CarWashesCreate
from car_washes.views import CarWashesListView

urlpatterns = (
    path('car_washes/', CarWashesCreate.as_view(), name='api car wash create'),
)
