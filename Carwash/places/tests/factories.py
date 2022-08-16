import factory
from faker import Faker

from places.models import CarWashes, Places


faker = Faker()

class PlacesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Places

    places_name = factory.LazyAttribute(lambda _: faker.name())
