from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from places.models import Places
from places.serializers import PlacesSerializer
from places.tests.factories import PlacesFactory

