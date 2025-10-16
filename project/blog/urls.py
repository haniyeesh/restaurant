from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', blog , name = 'blog'),
    path('single_blog/<int:blog_id>/' ,  single_blog , name='single_blog')  ,
    path('search_blog/', search_blog , name = 'search_blog'),

    
]