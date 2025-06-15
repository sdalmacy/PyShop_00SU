from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    wishlist = models.ManyToManyField('products.Product', blank=True, related_name='wishlisted_by')

    def __str__(self):
        return self.user.username

    def add_to_wishlist(self, product):
        """Add a product to the client's wish list."""
        self.wishlist.add(product)

    def wishlist_suggestions(self):
        """Return products from the wish list which can be used for suggestions."""
        return self.wishlist.all()


class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}"
