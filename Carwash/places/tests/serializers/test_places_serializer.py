from django.test import TestCase

from places.models import Places
from places.tests.factories import PlacesFactory
from places.serializers import PlacesSerializer


class PlacesSerializerTest(TestCase):
    def setUp(self):
        self.place = PlacesFactory()

    def test_instance_data(self):
        serializer = PlacesSerializer(
            instance=self.place
        )

        self.assertEqual(
            serializer.data['place_name'],
            self.place.places_name
        )

    def test_validation(self):
        place_data = {
            'place_name': 'some name'
        }

        serializer = PlacesSerializer(
            data=place_data
        )

        self.assertTrue(serializer.is_valid())
