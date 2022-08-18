from django.urls import path

from carwash_services.views import ServiceView, CarwashServicesView

url_patterns = (

    path('services/', ServiceView.as_view({'get': 'list'}), name='services'),
    path('carwash_services/', CarwashServicesView.as_view({'get': 'list'}), name='carwash_services')

)
