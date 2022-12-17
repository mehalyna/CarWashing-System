import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.test import Client

from order_details.views import OrderDetailViewSet
from order_details.tests.factories import OrderDetailFactory, OrderFactory, \
                                          CWPlacesFactory, ServiceFactory


class TestOrder(APITestCase):
    def setUp(self):
        self.client = Client()
        self.orderdetail = OrderDetailFactory(order=OrderFactory(),
                                              service=ServiceFactory(),
                                              carwash_place=CWPlacesFactory(),
                                              price=10.5,
                                              duration=15,
                                              start_time=datetime.time(18, 0, 0))
        self.client.login(email='user@user.com', password='12341234')

    # def test_OrderDetailViewSet(self):
    #     url = reverse(OrderDetailViewSet)
    #     data = '{"price": "10.5", "duration": "15", "start_time": "18:00:00"}'
    #     response = self.client.post(url, data, format='json')

    def test_unauthorized_user(self):
        self.client.logout()
        url = reverse('users-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
