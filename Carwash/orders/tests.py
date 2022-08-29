import datetime
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
        self.client.force_login(self.account)
        self.order_object = {
            'user': self.user.id,
            'car_wash': self.car_wash.id,
            'order_current_status': 'New',
            'order_date_time': datetime.datetime.now(),
            'execution': datetime.datetime.now(),
        }
        self.order_url = 'http://127.0.0.1:8000/orders/'

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

    def test_successful_post_request(self):
        """Test if object is successfully posted"""

        response = self.client.post(
            self.order_url,
            self.order_object,
        )

        actual = response.status_code
        expected = 201
        self.assertEqual(
            actual,
            expected
        )

    def test_successful_get_request(self):
        """Test if object is returned correctly with get request"""

        post = self.client.post(
            self.order_url,
            self.order_object,
        )

        posted_object_id = post.json()['id']
        response = self.client.get(f'{self.order_url}{posted_object_id}/')
        response_object_id = response.json()['id']

        self.assertEqual(
            response_object_id,
            posted_object_id,
        )

    def test_successful_put_request(self):
        """Test if object is successfully updated with put request"""

        post = self.client.post(
            self.order_url,
            self.order_object,
        )

        posted_object_id = post.json()['id']
        self.order_object['order_current_status'] = 'Changed'
        
        response = self.client.put(
            f'{self.order_url}{posted_object_id}/',
            self.order_object,
        )

        changed_object = self.client.get(
            f'{self.order_url}{posted_object_id}/',
        )

        actual = changed_object.json()['order_current_status']
        expected = self.order_object['order_current_status']

        self.assertEqual(
            actual,
            expected,
        )

    def test_successful_delete_request(self):
        """Test if object is deleted successfully with delete request"""

        post = self.client.post(
            self.order_url,
            self.order_object,
        )

        posted_object_id = post.json()['id']

        response = self.client.delete(
            f'{self.order_url}{posted_object_id}/',
        )

        actual = delete.status_code
        expected = 204

        self.assertEqual(
            actual,
            expected,
        )
