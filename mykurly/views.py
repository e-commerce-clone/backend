from django.shortcuts import render
from django.contrib.auth import authenticate
from accounts.models import Profile
from django.contrib.auth.models import User as auth_User
# Create your views here.


def order_list(request):
    return render(request, 'mykurly/mykurly_order_list.html')


def order_view(request):
    return render(request, 'mykurly/mykurly_orderview.html')


def review(request):
    return render(request, 'mykurly/mykurly_review.html')


def review_register(request):
    return render(request, 'mykurly/mykurly_review_register.html')


def information(request):
    if request.method == "POST":
        id = request.POST.get("id")
        pw = request.POST.get("confirm_password")
        try:
            user = authenticate(username=id, password=pw)
            return render(request, 'mykurly/mykurly_information_modify.html')
        except:
            pass
    return render(request, 'mykurly/mykurly_information.html')


def information_modify(request):
    return render(request, 'mykurly/mykurly_information_modify.html')


def delivery_list(request):
    return render(request, 'mykurly/mykurly_delivery_list.html')


def delivery_modify(request):
    return render(request, 'mykurly/mykurly_delivery_modify.html')


def address_search(request):
    return render(request, 'mykurly/mykurly_address_search.html')


def withdrawal(request):
    return render(request, 'mykurly/mykurly_withdrawal.html')
