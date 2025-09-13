from django.shortcuts import render,redirect
from menu.models import Category,Food
# from cart.cart import*
from .models import Idea,Custumer_Email,Reservations
# from account.models import Customer
from django.shortcuts import render,get_object_or_404
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    category = Category.objects.all()
    return render(request, 'menu.html', {'category':category})


def about(request):
    ideas = Idea.objects.all()
    return render(request, 'about.html', {'ideas': ideas})


def contact(request):
    return render(request, 'contact.html')


def search(request):
    query = request.GET.get('q')
    result =[]
    if query:
        result = Food.objects.filter(name__icontains = query)
    return render(request, 'search.html' , {'result' : result , 'query' : query})


def idea_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('user_login')
        else:
            name = request.user.username
            text = request.POST.get('text')
            email = request.user.email
            Idea.objects.create(
                name=name,
                email=email,
                text=text,
            )
            return redirect('contact')
    return render (request , 'contact.html')
     
        
def email_success(request):
    return render(request, 'email_success.html')


def custumer_email(request):
    if request.method=='POST':
        email = request.POST.get('custumar_email')
        
        Custumer_Email.objects.create(email = email   
        )
    return redirect ('email_success')


def reserve(request):
    user = request.user
    if not request.user.is_authenticated:
        return redirect('user_login')
    elif user.is_authenticated and user.role == "manager":
        reservations = Reservations.objects.all()
        return render(request, 'reserve_list.html',{'reservations': reservations })
    else:
        existing_reservation = Reservations.objects.filter(customer = request.user).first()
        if existing_reservation:
            return render(request, "reserve_success.html", {'reservation' : existing_reservation})
        else: 
            if request.method =="POST":
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                guest = request.POST.get('guests')
                date = request.POST.get('date')
                time = request.POST.get('time')
                note = request.POST.get('notes')
                
                reservation = Reservations(name=name,
                                        phone=phone,
                                        guest = guest,
                                        date=date,
                                        time=time,
                                        note=note)
                if request.user.is_authenticated:
                    reservation.customer = request.user
                reservation.save()
                return render(request, "reserve_success.html", {'reservation' : reservation})

    return render(request,'reserve.html')



