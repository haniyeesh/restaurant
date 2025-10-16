from django.urls import path
from .views import *

app_name = 'shopcart'

urlpatterns = [
    path('cart', cart_view , name = 'cart'),
    path('add_cart/<int:food_id>', add_to_cart , name = 'add_to_cart'),
    path('update_cart', update_cart , name = 'update_cart'),
     path('cart/remove/<int:food_id>/', remove_cart_item, name='remove_cart_item'),
    ]
