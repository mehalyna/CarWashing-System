import factory

from factory import fuzzy
from faker import Faker

from order_details.models import OrderDetail
from orders.models import Order
from carwash_services.models import Services
from CW_places.models import CWPlaces
from car_washes.models import CarWashes
from users.models import Users, Accounts
from places.models import Places

fake = Faker()


class PlacesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Places
        django_get_or_create = ('place_id',)

    place_id = factory.Sequence(lambda n: n)
    place_name = factory.Sequence(lambda p: f'place_{p}')

class AccountsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Accounts
        django_get_or_create = ('email', 'is_staff')

    email = fake.email()
    is_staff = False


class UsersFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Users
        django_get_or_create = ('account',)

    phone_number = fake.phone_number()
    full_name = fake.name()
    user_location = fake.address()
    account = factory.SubFactory(AccountsFactory)


class CarWashesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarWashes
        django_get_or_create = ('car_wash_name',)

    car_wash_name = fuzzy.FuzzyAttribute(lambda: f'{fake.name()} wash')
    car_wash_address = fake.address()
    quantity_of_places = fuzzy.FuzzyInteger(1, 100)


class ServiceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Services
        django_get_or_create = ('service_name', 'service')

    service_name = fuzzy.FuzzyChoice(choices=
            ['inside', 'outside', 'combine', 'engin_wash'])
    service = fuzzy.FuzzyInteger(1, 1000)


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Order
        django_get_or_create = ('car_wash', 'user',)

    car_wash = factory.SubFactory(CarWashesFactory)
    user = factory.SubFactory(UsersFactory)
    order_current_status = fuzzy.FuzzyChoice(choices=['Cancelled', 'Ready'] + ['Confirmed']*10)
    order_date_time = fake.time()
    execution = fake.time()


class CWPlacesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CWPlaces
        django_get_or_create = ('place', 'carwash',)

    carwash_place = factory.Sequence(lambda n: n)
    place = factory.SubFactory(PlacesFactory)
    carwash = factory.SubFactory(CarWashesFactory)
    is_free = fuzzy.FuzzyChoice(choices=(True, True, True, True, False,))


class OrderDetailFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = OrderDetail
        django_get_or_create = ('order', 'service', 'carwash_place',
                                'price', 'duration', 'start_time',)

    order = factory.SubFactory(OrderFactory)
    service = factory.SubFactory(ServiceFactory)
    carwash_place = factory.SubFactory(CWPlacesFactory)
    price = fuzzy.FuzzyFloat(1, 1000)
    duration = fuzzy.FuzzyInteger(1, 720)
    start_time = fake.time()
