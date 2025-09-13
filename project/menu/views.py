from django.shortcuts import render
from .models import Food,Category
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

def category1(request, category_id): 
    category = get_object_or_404(Category, id = category_id)
    food = Food.objects.filter(category = category)
    paginator = Paginator(food, 2) 
    page_number = request.GET.get('page')    #first get is a dict sec is keys value
    page_obj = paginator.get_page(page_number)
    return render(request, 'burger.html', {'food': food, 'category': category, 'page_obj':page_obj})






