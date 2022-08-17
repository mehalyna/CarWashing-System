import datetime
import factory

from car_washes.models import CarWashes
from orders.models import Order
from users.models import Accounts, Users


class AccountFactory(factory.Factory):

    class Meta:
        model = Accounts
    
    email = 'arthur.dent@the-guide.com'
    is_staff = False


class UserFactory(factory.Factory):

    class Meta:
        model = Users

    phone_number = '+359-897-111-222'
    full_name = 'Arthur Dent'
    user_location = 'Earth'
    account = AccountFactory()


class CarWashFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarWashes
    
    car_wash_name = 'Car Wash at the end of the Universe'
    car_wash_address = 'At the end of the Universe'
    quantity_of_places = 1


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Order
    
    car_wash = CarWashFactory()
    user = UserFactory()
    order_current_status = 'New'
    order_date_time = datetime.datetime.now()
    execution = datetime.datetime.now()
