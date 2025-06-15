from django.shortcuts import render


def checkout(request):
    """Display payment options for PayPal and Bitcoin."""
    return render(request, 'payments/checkout.html')
