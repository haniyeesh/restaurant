from django.shortcuts import render ,redirect, get_object_or_404
from . models import *
from menu.models import Food
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_or_create_cart
from django.contrib import messages

def cart_view(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()
    total_price = sum(item.get_total_price() for item in items)
    
    
    return render(request, 'cart.html', {'cart': cart, 'items':items, 'total_price': total_price})


def add_to_cart(request,food_id):
    if request.method == 'POST':
        cart = get_or_create_cart(request)
        food_id = request.POST.get('food_id')
        quantity = int(request.POST.get('quantity', 1))
        food = get_object_or_404(Food, id = food_id)
       
        cart_item = Cart_item.objects.filter(cart= cart, product= food).first()
        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item, created = Cart_item.objects.get_or_create(
                cart = cart,
                quantity = quantity,
                product = food,
                price_at_added=food.price
            )
    messages.success(request, "محصول به سبد خرید اضافه شد")
    return redirect ('shopcart:cart')
 
    

def remove_cart_item(request, food_id):
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(Cart_item, cart=cart, product_id=food_id)
    cart_item.delete()  # حذف آیتم
    return render (request,'cart.html')  # بازگشت به صفحه سبد خرید
 


def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        food_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))

        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(Cart_item, cart=cart, product_id=food_id)

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            total_price_item = cart_item.get_total_price()
        else:
            cart_item.delete()
            total_price_item = 0

        # محاسبه قیمت کل سبد
        items = cart.items.all()
        total_price_cart = sum(item.get_total_price() for item in items)

        return JsonResponse({
            'item_total': total_price_item,
            'cart_total': total_price_cart
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
 