from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User as auth_User
from django.contrib.auth.hashers import make_password
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    # csrf_token 무시하기 위한 @csrf_exempt

# SMTP 관련 인증 : 이메일 인증 Gmail 이용
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .token import account_activation_token

# Create your views here


def signup(request):        # 회원가입 뷰
    if request.method == "GET":
        return render(request, 'accounts/signup.html')

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

        if (birthday_year and birthday_month and birthday_day):
            age = 2021 - int(birthday_year) + 1
            birthday = f'{birthday_year}-{birthday_month}-{birthday_day}'
        else:
            age = None
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
                         email=email,
                         is_active=False)

        user_info = Profile(user=user,
                            email=email,
                            person_name=person_name,
                            phone_number=phone_number,
                            home_address=home_address,
                            birthday=birthday,
                            age=age)
        user.save()
        user_info.save()
        # 이메일 인증을 위한 추가 설정, 회원가입 완료 시 이메일 인증을 위한 이메일 전송
        current_site = get_current_site(request)
        message = render_to_string('accounts/activation_email.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': account_activation_token.make_token(user),
                                   })
        mail_title = "계정 활성화 확인 이메일"
        mail_to = request.POST["email"]
        email = EmailMessage(mail_title, message, to=[mail_to])
        email.send()
        return render(request, 'accounts/signup_done.html', res_data)


def login(request):     # 로그인 뷰 : django auth login
    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=name, password=pwd)
        if user is not None:
            auth_login(request, user)
            return redirect("/")

    return render(request, "accounts/login.html")


def find_id(request):
    return render(request, "accounts/find_id.html")


def find_pw(request):
    return render(request, "accounts/find_pw.html")


def logout(request):    # 로그아웃 뷰 : django auth logout
    auth_logout(request)
    return redirect("/")


@csrf_exempt
def id_overlap_check(request):  # 아이디 중복 확인 뷰
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
def email_overlap_check(request):   # 이메일 중복 확인 뷰
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


def activate(request, uidb64, token):   # 이메일 인증 뷰 : 이메일 인증이 완료되면 계정활성화
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = auth_User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, auth_User.DoesNotExist):
        user = None
        print('에러발생')
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return redirect("/")
    else:
        return render(request, 'shop/main.html', {'error': '계정 활성화 오류'})
    return
