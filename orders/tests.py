from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from products.models import Product
from .models import Order, OrderItem


class OrderModelTest(TestCase):
    def test_create_order_and_item(self):
        user = get_user_model().objects.create(username='tester')
        product = Product.objects.create(name='Prod', price=1, stock=1, image_url='img')
        order = Order.objects.create(user=user)
        item = OrderItem.objects.create(order=order, product=product, quantity=2, price=3.0)

        self.assertEqual(str(order), f"Order #{order.pk}")
        self.assertEqual(str(item), f"2 x {product}")


class IndexViewTest(TestCase):
    def test_index_returns_home(self):
        response = self.client.get(reverse('orders:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Orders Home')
