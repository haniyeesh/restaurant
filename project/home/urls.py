from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name = 'home'),
    path('about', about , name = 'about'),
    path('menu/', menu , name = 'menu'),
    path('contact', contact , name = 'contact'),
    path('search', search , name = 'search'),
    path('idea_view', idea_view , name = 'idea_view'),
    path('custumer_email', custumer_email , name = 'custumer_email'),
    path('email_success', email_success , name = 'email_success'),
    path('reserve', reserve , name = 'reserve'),
    # path('reservation/<int:reservation_id>/', reserve_status , name = 'reserve_status'),
 
]