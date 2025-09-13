from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from .models import Profile,User,Manager_permission
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib import messages
from home.models import Reservations


def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                    login(request, user)
                    user = request.user
                    if user.role == "manager":
                        return render(request, 'manage.html')
                    else:
                        return redirect('/')
            else:
                error = "نام کاربری یا رمز عبور اشتباه است"
        except User.DoesNotExist:
            error = "نام کاربری یا رمز عبور اشتباه است"
        return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error = "رمز عبور و تایید آن مطابقت ندارند"
            return render(request, 'signup.html', {'error': error})

        if User.objects.filter(username=username).exists():
            error = "نام کاربری قبلا ثبت شده است"
            return render(request, 'signup.html', {'error': error})

        hashed_password = make_password(password1)
        user = User.objects.create(
        username=username,
        email=email,
        phone_number = phone_number,
        password=hashed_password
        )
        return render(request, 'success.html')
    return render(request, 'signup.html')


def success(request):
    return render (request, 'success.html')


def psw(request):
    User = get_user_model()
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "رمزها یکسان نیستند.")
            return render(request, "password.html")

        try:
            user = User.objects.get(phone_number=phone) # ← اینجا دقیقا مدل یوزر خودتو میاره
        except User.DoesNotExist:
            user = None

        if user:
            user.set_password(new_password)
            user.save()
            messages.success(request, "رمز جدید ذخیره شد.")
            return redirect("user_login")
        else:
            messages.error(request, "این شماره موبایل ثبت نشده است لطفا اول ثبت نام کنید.")


    return render (request, 'password.html')


def profile(request):
    customer_id =request.user.id
    if not customer_id:
        return redirect('user_login')
    customer = User.objects.get(id=customer_id)
    profile = request.user.profile
    return render(request, 'profile.html', {'customer': customer, 'profile':profile})


def edit_profile(request):
    customer_id = request.user.id
    customer = User.objects.get(id=customer_id)
    profile = customer.profile
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # avatar = request.FILES.get('avatar')
        # if avatar:
        #     profile.avatar =avatar
        profile.email = email
        profile.first_name = first_name
        profile.last_name = last_name
        profile.phone = phone 
        profile.address = address
        profile.save()
        return redirect('profile')
          
    return render(request, 'profile_edit.html', {'customer' : customer, 'profile' : profile})


def logout_view(request):
    logout(request)
    return redirect('/')

