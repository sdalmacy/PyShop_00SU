from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Order


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=pid)
        amount = product.price * qty
        items.append({'product': product, 'quantity': qty, 'amount': amount})
        total += amount
    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})


def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        for pid, qty in cart.items():
            product = get_object_or_404(Product, pk=pid)
            amount = product.price * qty
            Order.objects.create(product=product, quantity=qty, amount=amount, paid=True)
        request.session['cart'] = {}
        return render(request, 'cart/checkout_success.html')
    return render(request, 'cart/checkout.html')
