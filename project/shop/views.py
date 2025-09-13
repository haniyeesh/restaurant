from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,CartItem
from menu.models import Food
from .cart import *
def cart(request):
    return render(request, "cart.html")

#

def view_cart(request):
    cart = get_or_create_cart(request)
    items = get_cart_item(cart)
    total = calculate_total(cart)
    
    return render(request, 'cart.html', {'cart':cart, 'items':items, 'total':total})
    

def add_to_cart_view(request):
    if request.method == "POST":
        food_id = request.POST.get('food_id')
        quantity = int(request.POST.get('quantity', 1))
        food = get_object_or_404(Food, id=food_id)
        cart = get_or_create_cart(request)
        add_to_cart(cart, food, quantity)
    return redirect('menu')
    