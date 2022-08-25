import json

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from places.tests.factories import PlacesFactory

user_model = get_user_model()


class PlacesViewsTests(APITestCase):
    def setUp(self):
        self.place = PlacesFactory()
        user = user_model.objects.create(email='testing@mail.com', password='123456')
        self.client.force_authenticate(user)

    def test_get_place_when_user_is_authenticated_expect_200(self):
        url = reverse('Places-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_place_when_user_is_not_authenticated_except_401(self):
        url = reverse('Places-list')
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_places_when_user_is_authenticated_expect_201(self):
        url = reverse('Places-list')
        response = self.client.post(url, self.place.__dict__)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_places_when_user_is_authenticated_expect_200(self):
        url = reverse('Places-detail', kwargs={'pk': self.place.pk})
        data = {
            'place_name': 'edited name'
        }
        response = self.client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_places_when_user_is_authenticated_expect_204(self):
        url = reverse('Places-detail', kwargs={'pk': self.place.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        