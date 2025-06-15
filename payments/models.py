from django.db import models
from orders.models import Order


class Payment(models.Model):
    order = models.ForeignKey(Order, related_name="payments", on_delete=models.CASCADE)
    amount = models.FloatField()
    provider = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order_id}"
