from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from car_washes.tests.factories import CarWashesFactory

from users.models import Users

user_model = get_user_model()


class CarWashesViewSetTests(APITestCase):
    def setUp(self):
        self.client = Client()
        self.car_wash = CarWashesFactory()
        user = user_model.objects.create(email='test@mail.com', password='123456')
        self.client.force_login(user)

    def test_get_car_wash__when_user_is_authenticated__expect_200(self):
        url = reverse('carwashes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_car_wash__when_user_is_not_authenticated__except_403(self):
        url = reverse('carwashes-list')
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_post_car_washes__when_user_is_authenticated__expect_201(self):
        url = reverse('carwashes-list')
        response = self.client.post(url, self.car_wash.__dict__)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_car_washes__when_user_is_authenticated__expect_200(self):
        url = reverse('carwashes-detail', kwargs={'pk': self.car_wash.pk})
        data = {
            'car_wash_name': 'edited name',
            'car_wash_address': 'edited address',
            'quantity_of_places': 12,
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_car_washes__when_user_is_authenticated__expect_204(self):
        url = reverse('carwashes-detail', kwargs={'pk': self.car_wash.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
