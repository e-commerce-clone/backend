from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User as auth_User
from django.contrib.auth.hashers import make_password
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    elif request.method == "POST":
        username = request.POST.get('id', None)
        password = request.POST.get('pw', None)
        person_name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        user_address = request.POST.get('user_address', None)
        user_address_detail = request.POST.get('user_address_detail', None)
        birthday_year = request.POST.get('year', None)
        birthday_month = request.POST.get('month', None)
        birthday_day = request.POST.get('day', None)
        age = 2021 - int(birthday_year) + 1

        if (birthday_year and birthday_month and birthday_day):
            birthday = f'{birthday_year}-{birthday_month}-{birthday_day}'
        else:
            birthday = None

        if (user_address and user_address_detail):
            home_address = f'{user_address}, {user_address_detail}'
        else:
            home_address = None

        res_data = {
            'username': username,
            'person_name': person_name,
            'email': email
        }
        user = auth_User(username=username,
                         password=make_password(password),
                         email=email)

        user_info = Profile(user=user,
                            email=email,
                            person_name=person_name,
                            phone_number=phone_number,
                            home_address=home_address,
                            birthday=birthday,
                            age=age)
        user.save()
        user_info.save()
        return render(request, 'accounts/register_done.html', res_data)


def login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=name, password=pwd)
        if user is not None:
            auth_login(request, user)
            return redirect("/")

    return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect("/")

def findid(request):
    return render(request, 'accounts/find_id.html')   

def findpw(request):
    return render(request, 'accounts/find_pw.html')  






@csrf_exempt
def id_overlap_check(request):
    username = request.GET.get('username')
    try:
        user = auth_User.objects.get(username=username)
    except:
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)

@csrf_exempt
def email_overlap_check(request):
    email = request.GET.get('email')
    try:
        user = Profile.objects.get(email=email)
    except:
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)