from django.urls import reverse
from django.test import TestCase
from .models import Product, Offer


class ProductModelTest(TestCase):
    def test_create_and_retrieve_product(self):
        product = Product.objects.create(
            name='Django Mug', price=9.99, stock=10, image_url='http://example.com/mug.jpg'
        )
        self.assertEqual(Product.objects.count(), 1)
        retrieved = Product.objects.first()
        self.assertEqual(retrieved.name, 'Django Mug')
        self.assertEqual(str(retrieved.id), str(product.id))


class OfferModelTest(TestCase):
    def test_create_offer(self):
        offer = Offer.objects.create(code='SPRING', description='Spring Sale', discount=10.0)
        self.assertEqual(Offer.objects.count(), 1)
        self.assertEqual(offer.code, 'SPRING')


class IndexViewTest(TestCase):
    def test_index_displays_products(self):
        Product.objects.create(name='Django Shirt', price=20, stock=5, image_url='http://example.com/shirt.jpg')
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Django Shirt')


class NewViewTest(TestCase):
    def test_new_returns_message(self):
        response = self.client.get(reverse('products:new'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to PyShop New Arrivals')
