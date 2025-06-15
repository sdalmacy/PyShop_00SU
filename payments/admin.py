from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "provider", "timestamp")


admin.site.register(Payment, PaymentAdmin)
