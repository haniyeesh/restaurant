from django.shortcuts import render ,redirect
from .utils import get_or_create_cart

def cart_data(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()
    total_price = sum(item.quantity * item.price_at_added for item in items)
   
    
    return{'cart': cart, 'items':items, 'total_price': total_price, 'cart_count': cart.total_quantity()}