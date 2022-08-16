from django.test import TestCase

from places.models import Places
from places.tests.factories import PlacesFactory


class PlacesModelTests(TestCase):
    def setUp(self):
        self.place = PlacesFactory()

    def test_places_create_when_fields_are_valid_expect_success(self):
        self.assertIsNotNone(self.place.pk)

    def test_places_str_method_when_name_is_correct_expect_equal(self):
        self.assertEqual(str(self.place), self.place.places_name)

    def test_places_str_method_when_name_is_incorrect_expect_not_equal(self):
        self.assertNotEqual(str(self.place), 'Wrong name')
