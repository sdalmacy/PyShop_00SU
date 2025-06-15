from django.test import TestCase, Client


class ProductViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_product_index_template(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

