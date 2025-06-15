from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from products.models import Product
from orders.models import Order
from .models import Payment


class PaymentModelTest(TestCase):
    def test_create_payment(self):
        user = get_user_model().objects.create(username='payer')
        product = Product.objects.create(name='Prod', price=2, stock=1, image_url='img')
        order = Order.objects.create(user=user)
        payment = Payment.objects.create(order=order, amount=2, provider='cash')

        self.assertEqual(str(payment), f"Payment for Order #{order.pk}")


class IndexViewTest(TestCase):
    def test_index_returns_home(self):
        response = self.client.get(reverse('payments:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Payments Home')
