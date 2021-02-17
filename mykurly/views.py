from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate
from accounts.models import Profile
from shop.models import Product
from photo.models import Product_photo, Review_photo
from mykurly.models import Review
from django.http import JsonResponse
from django.contrib.auth.models import User as auth_User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def order_list(request):
    return render(request, 'mykurly/mykurly_order_list.html')


@login_required
def order_view(request):
    return render(request, 'mykurly/mykurly_orderview.html')


@login_required
def review(request):
    return render(request, 'mykurly/mykurly_review.html')


@login_required
def review_register(request, username, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        photo = get_object_or_404(Product_photo, product=product)
        data = {
            'product_name': product.name,
            'photo': photo.main_image,
        }
        return render(request, 'mykurly/mykurly_review_register.html', data)

    elif request.method == "POST":
        title = request.POST.get('subject')
        contents = request.POST.get('contents')
        try:
            images = request.FILES['file[]']
        except:
            images = None

        reviews = Review.objects.filter(product=product)
        count = 1
        for _ in reviews:
            count += 1

        user = get_object_or_404(auth_User, username=username)
        writer = get_object_or_404(Profile, user=user)
        review = Review(product=product,
                        writer=writer,
                        title=title,
                        contents=contents,
                        product_image=images,
                        count=count)
        review.save()
        return redirect('mykurly:review')


@login_required
def information(request):
    if request.method == "POST":
        id = request.POST.get("id")
        pw = request.POST.get("confirm_password")
        user = authenticate(username=id, password=pw)
        if user is not None:
            return redirect('mykurly:information_modify', user.pk)
        else:
            error = {"error": "비밀번호가 일치하지 않습니다."}
            return render(request, 'mykurly/mykurly_information.html', error)
    else:
        return render(request, 'mykurly/mykurly_information.html')


@login_required
def information_modify(request, pk):
    if request.method == "GET":
        user = get_object_or_404(auth_User, pk=pk)
        profile = get_object_or_404(Profile, user=user)
        birth = str(profile.birthday).split('-')
        data = {
            "id": user.username,
            "person_name": profile.person_name,
            "email": profile.email,
            "phone_number": profile.phone_number,
            "birth_year": birth[0],
            "birth_month": birth[1],
            "birth_day": birth[2],
        }
        return render(request, 'mykurly/mykurly_information_modify.html', data)
    else:
        id = request.POST.get('id')
        password = request.POST.get('originalPassword')
        new_pw = request.POST.get('pw')
        person_name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('mobileInp')
        birthday_year = request.POST.get('year')
        birthday_month = request.POST.get('month')
        birthday_day = request.POST.get('day')
        age = 2021 - int(birthday_year) + 1
        birthday = f'{birthday_year}-{birthday_month}-{birthday_day}'
        user = authenticate(username=id, password=password)

        if user is not None:
            user.set_password(new_pw)
            user.email = email
            user.save()
            profile = get_object_or_404(Profile, user=user)
            profile.person_name = person_name
            profile.email = email
            profile.phone_number = phone_number
            profile.birthday = birthday
            profile.age = age
            profile.save()
            return redirect('mykurly:information_modify', pk)
        else:
            error = {'error': "현재 비밀번호가 일치하지 않습니다."}
            JsonResponse(error)


@login_required
def delivery_list(request):
    return render(request, 'mykurly/mykurly_delivery_list.html')


@login_required
def delivery_modify(request):
    return render(request, 'mykurly/mykurly_delivery_modify.html')


@login_required
def address_search(request):
    return render(request, 'mykurly/mykurly_address_search.html')


@login_required
def withdrawal(request, pk):
    if request.method == "POST":
        user = get_object_or_404(auth_User, pk=pk)
        password = request.POST.get('password')
        print(f'아이디:{user.username} 비밀번호:{password}')
        user = authenticate(username=user.username, password=password)
        if user is not None:
            user.delete()
            return redirect('/')
        else:
            print("비밀빈호 불일치")
            error = {'error': "비밀번호가 일치하지 않습니다."}
            return render(request, 'mykurly/mykurly_withdrawal.html', error)
    return render(request, 'mykurly/mykurly_withdrawal.html')
