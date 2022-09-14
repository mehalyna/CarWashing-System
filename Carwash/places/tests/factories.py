import factory
from faker import Faker

from places.models import Places


faker = Faker()

class PlacesFactory(factory.django.DjangoModeFactory):
    class Meta:
        model = Places

    place_name = factory.LazyAttribute(lambda _: faker.name())
    