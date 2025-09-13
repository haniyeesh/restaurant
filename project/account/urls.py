from django.urls import path
from .views import *

urlpatterns = [
    path('user_login/', user_login , name = 'user_login'),
    path('signup/' ,   signup , name='signup')  ,
    path('profile/' ,   profile , name='profile'),
    path('edit_profile/' ,   edit_profile , name='edit_profile'),
    path('logout', logout_view, name='logout' ),
    path('success', logout_view, name='logout' ),
    path('psw', psw, name='psw' ),
]