from django.urls import path
from .views import *


urlpatterns = [

    path('manager', manager, name='manager' ),
    path('table', table, name='table' ),
    path('reservation/<int:reservation_id>/', reserve_status , name = 'reserve_status'),
    
]