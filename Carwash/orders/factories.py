import datetime
import factory

from car_washes.models import CarWashes
from orders.models import Order
from users.models import Accounts, Users


class AccountFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Accounts
        django_get_or_create = ('email',)

    email = 'arthur.dent@the-guide.com'
    password = '424242'


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Users
        django_get_or_create = ('phone_number',)
    
    phone_number = '4242424242'
    full_name = 'Arthur Dent'
    user_location = 'Earth'
    account = factory.SubFactory(AccountFactory)


class CarWashFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarWashes
    
    car_wash_name = 'Car Wash at the end of the Universe'
    car_wash_address = 'At the end of the Universe'
    quantity_of_places = 1


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Order
        django_get_or_create = ('user', 'car_wash')
    
    car_wash = factory.SubFactory(CarWashFactory)
    user = factory.SubFactory(UserFactory)
    order_current_status = 'New'
    order_date_time = datetime.datetime.now()
    execution = datetime.datetime.now()
