from django.urls import path
from .views import *


urlpatterns = [
    path('category1/<int:category_id>', category1 , name = 'category1')]
