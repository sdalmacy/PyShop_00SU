from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist')
]
