from django.test import TestCase
from django.urls import reverse

from orders.factories import UserFactory, CarWashFactory, OrderFactory
from orders.models import Order

class TestOrders(TestCase):

    def setUp(self) -> None:
        self.user = UserFactory
        self.car_wash = CarWashFactory
        self.order = OrderFactory
        return super().setUp()

    def test_proper_connection(self):
        user = {
            'phone_number': self.user.phone_number,
            'full_name': self.user.full_name,
            'user_location': self.user.user_location,
            'account': self.user.account,
        }
        data = {
            'car_wash': self.order.car_wash,
            'user': self.order.user,
            'order_current_status': self.order.order_current_status,
            'execution': self.order.execution,
        }
        user_response = self.client.post('127.0.0.1:8000', data=user)
        data_response = self.client.post(reverse('orders'), data=data)
        order = Order.objects.all()
        print(user_response)
        print(data_response.status_code)
