from django.urls import reverse
from django.test import TestCase
from .models import Account


class AccountModelTest(TestCase):
    def test_str_representation(self):
        account = Account.objects.create(username='user1', email='user1@example.com')
        self.assertEqual(str(account), 'user1')


class IndexViewTest(TestCase):
    def test_index_returns_home(self):
        response = self.client.get(reverse('accounts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Accounts Home')
