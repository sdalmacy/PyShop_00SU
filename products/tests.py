from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            name='Test Product',
            price=9.99,
            stock=10,
            image_url='http://example.com/image.jpg'
        )
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 9.99)
        self.assertEqual(product.stock, 10)
        self.assertEqual(product.image_url, 'http://example.com/image.jpg')

class IndexViewTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name='Index Product',
            price=1.0,
            stock=5,
            image_url='http://example.com/img.jpg'
        )

    def test_index_view_displays_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('products', response.context)
        self.assertEqual(len(response.context['products']), 1)

class NewViewTest(TestCase):
    def test_new_view_returns_message(self):
        response = self.client.get('/products/new/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to PyShop New Arrivals')
