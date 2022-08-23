from rest_framework.test import APITestCase

from orders import factories
from orders.models import Order


class TestOrders(APITestCase):
    """
    Test CRUD operations on Order model.
    """

    def setUp(self) -> None:
        """Create and save test instances with random values"""

        self.account = factories.AccountFactory.create()
        self.user = factories.UserFactory.create()
        self.car_wash = factories.CarWashFactory.create()
        self.order = factories.OrderFactory.create()
        
    def test_successful_create_data(self):
        """Test if object is created and saved"""

        data = Order.objects.all()
        self.assertIsNotNone(data)
    
    def test_successful_delete_data(self):
        """Test if object is deleted"""

        instance = Order.objects.first()
        instance.delete()
        instance = Order.objects.all()
        self.assertEquals(len(instance), 0)

    def test_successful_update_data(self):
        """Test if object is updated"""

        new_order_status = 'Changed Status'
        instance = Order.objects.first()
        self.assertTrue(instance.order_current_status.startswith('New'))

        instance.order_current_status = new_order_status
        instance.save()

        changed_instance = Order.objects.get(pk=instance.pk)

        actual = changed_instance.order_current_status
        self.assertEqual(new_order_status, actual)
