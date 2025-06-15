from django.contrib import admin
from .models import Client, Address


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'wishlist_count')

    def wishlist_count(self, obj):
        return obj.wishlist.count()
    wishlist_count.short_description = 'Wishlist Items'


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('client', 'street', 'city', 'country')
