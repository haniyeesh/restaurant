from django.urls import path
from .views import *
app_name = 'cart'
urlpatterns = [
    path('cart', cart , name = 'cart'),
    path('add_to_cart_view', add_to_cart_view , name = 'add_to_cart_view'),]
