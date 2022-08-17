from django.urls import reverse
from django.test import Client

from rest_framework import status
from rest_framework.test import APITestCase

from car_washes.models import CarWashes
from car_washes.serializers import CarWashesSerializer
from car_washes.tests.factories import CarWashesFactory

from users.tests.factories import UsersFactory
from users.models import Users


class CarWashesViewSetTests(APITestCase):
    def setUp(self):
        self.client = Client()
        self.car_wash = CarWashesFactory
        # self.user = Users.objects.create(
        #     phone_number='1231412',
        #     full_name='some full name',

        # )
        # self.client.login(email=self.user.email, password='adm1n')
    # def test_unauthorized_user(self):
    #     self.client.logout()
    #     url = reverse('users-list')
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_authorized_user(self):
    #     url = reverse('users-list')
    #     serializers = UsersSerializer(instance=Users.objects.all(), many=True)
    #     response = self.client.get(url, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.json(), serializers.data)

    # def test_create_car_wash__when_all_fileds_are_valid__expect_success(self):
    #     self.client.post(url)

    def test_get_car_wash(self):
        url = reverse('carwashes-list')
        response = self.client.get(url, {'_id': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
