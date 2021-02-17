from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User as auth_User
from django.contrib.auth.hashers import make_password
from django.template import RequestContext
from django.contrib import messages
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    # csrf_token 무시하기 위한 @csrf_exempt
import string, random

# SMTP 관련 인증 : 이메일 인증 Gmail 이용
from django.contrib.sites.shortcuts import get_current_site  # request 를 보낸 사이트를 알려줌
from django.template.loader import render_to_string     # template 반환과 동시에 rendering 함.
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .token import account_activation_token

# Create your views here


def join(request):        # 회원가입 뷰
    if request.method == "GET":
        return render(request, 'accounts/join.html')

    elif request.method == "POST":
        username = request.POST.get('id', None)
        password = request.POST.get('pw', None)
        person_name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        user_address = request.POST.get('user_address', None)
        user_address_detail = request.POST.get('user_detail_address', None)
        birthday_year = request.POST.get('year', None)
        birthday_month = request.POST.get('month', None)
        birthday_day = request.POST.get('day', None)

        age = 2021 - int(birthday_year) + 1
        birthday = f'{birthday_year}-{birthday_month}-{birthday_day}'
        home_address = f'{user_address}, {user_address_detail}'

        first_name = person_name[1:3]
        last_name = person_name[0]

        res_data = {
            'username': username,
            'person_name': person_name,
            'email': email
        }
        user = auth_User(username=username,
                         password=make_password(password),
                         first_name=first_name,
                         last_name=last_name,
                         email=email,
                         is_active=False)
        user_info = Profile(user=user,
                            email=email,
                            person_name=person_name,
                            phone_number=phone_number,
                            home_address=home_address,
                            birthday=birthday,
                            age=age)
        try:
            user.save()  # 유저 저장
            user_info.save()  # 프로필 저장
        except:
            user.delete()
            print("회원가입 에러")
        # 이메일 인증을 위한 추가 설정, 회원가입 완료 시 이메일 인증을 위한 이메일 전송
        current_site = get_current_site(request)
        message = render_to_string('accounts/activation_email.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       # force_bytes : 인자값을 bytes 로 변형, encode 인코딩
                                       # user.pk = 57 -> force_bytes(user.pk) => b'57'
                                       # urlsafe_base64_encode(force_bytes(user.pk)) => b'NTc'
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': account_activation_token.make_token(user),
                                   })
        mail_title = "계정 활성화 확인 이메일"
        mail_to = request.POST["email"]
        email = EmailMessage(mail_title, message, to=[mail_to])
        email.send()
        return render(request, 'accounts/join_complete.html', res_data)


def mobile_join(request):
    if request.method == "GET":
        return render(request, 'accounts/mobile_join.html')

    elif request.method == "POST":
        username = request.POST.get('id', None)
        password = request.POST.get('pw', None)
        person_name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        user_address = request.POST.get('user_address', None)
        user_address_detail = request.POST.get('user_detail_address', None)
        birthday_year = request.POST.get('year', None)
        birthday_month = request.POST.get('month', None)
        birthday_day = request.POST.get('day', None)

        age = 2021 - int(birthday_year) + 1
        birthday = f'{birthday_year}-{birthday_month}-{birthday_day}'
        home_address = f'{user_address}, {user_address_detail}'

        first_name = person_name[1:3]
        last_name = person_name[0]

        res_data = {
            'username': username,
            'person_name': person_name,
            'email': email
        }

        user = auth_User(username=username,
                         password=make_password(password),
                         first_name=first_name,
                         last_name=last_name,
                         email=email,
                         is_active=False)
        user_info = Profile(user=user,
                            email=email,
                            person_name=person_name,
                            phone_number=phone_number,
                            home_address=home_address,
                            birthday=birthday,
                            age=age)
        try:
            user.save()  # 유저 저장
            user_info.save()  # 프로필 저장
        except:
            user.delete()
            print("회원가입 에러")
        # 이메일 인증을 위한 추가 설정, 회원가입 완료 시 이메일 인증을 위한 이메일 전송
        current_site = get_current_site(request)
        message = render_to_string('accounts/activation_email.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       # force_bytes : 인자값을 bytes 로 변형, encode 인코딩
                                       # user.pk = 57 -> force_bytes(user.pk) => b'57'
                                       # urlsafe_base64_encode(force_bytes(user.pk)) => b'NTc'
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': account_activation_token.make_token(user),
                                   })
        mail_title = "계정 활성화 확인 이메일"
        mail_to = request.POST["email"]
        email = EmailMessage(mail_title, message, to=[mail_to])
        email.send()
        return render(request, 'accounts/mobile_join_complete.html', res_data)


def login(request):     # 로그인 뷰 : django auth login
    template = "accounts/login.html"

    if request.method == "POST":
        name = request.POST.get('username') # id
        pwd = request.POST.get('password') # pw
        user = authenticate(username=name, password=pwd)
        try:
            check_user = auth_User.objects.get(username=name)
        except:     # 정보 부정확.
            return render(request, template)

        if check_user is not None:  # 계정이 있을 경우
            if (check_user.is_active == True):  # 계정 활성화일 경우
                try:    # 로그인 가능
                    auth_login(request, user)   # login 수행
                    # if (name == "admin"):
                    #     return render(request, "main/main.html", {'m_name': "admin"})
                    # profile = Profile.objects.get(user=user)
                    # person_name = profile.person_name
                    # data = {
                    #     'm_name': person_name,
                    # }
                    return render(request, "main/main.html")
                except:     # 아이디 비밀번호 불일치일 경우
                    error = 1
                    data = {'error': error, }
                    print(error, '아이디 비번 불일치')
                    return render(request, template, data)
            elif (check_user.is_active == False):   # 계정 활성화 아닐 경우
                error = 0
                data = {'error': error, }
                print(error, '계정활성화 필요')
                return render(request, template, data)
    return render(request, template)


def logout(request):    # 로그아웃 뷰 : django auth logout
    auth_logout(request)
    return redirect("/")


def findid(request):
    if request.method == 'POST':
        name = request.POST.get('srch_name')
        email = request.POST.get('srch_email')
        try:
            res_id = Profile.objects.get(person_name=name, email=email)
        except:
            return render(request, 'accounts/find_id_fail.html')

        if res_id is not None:
            res_data = {
                'username': res_id,
            }
            return render(request, 'accounts/find_id_ok.html', res_data)

    else:
        return render(request, 'accounts/find_id.html')


def findidok(request):
    return render(request, 'accounts/find_id_ok.html')


def findidfail(request):
    return render(request, 'accounts/find_id_fail.html')


def findpw(request):
    if request.method == 'POST':
        name = request.POST.get('srch_name')
        m_id = request.POST.get('srch_id')
        email = request.POST.get('srch_email')
        try:
            res_pw = auth_User.objects.get(username=m_id)
        except:
            return render(request, 'accounts/find_pw_fail.html')
        if res_pw is not None:
            res_data = {
                'username': name,
                'email': email,
            }
            return render(request, 'accounts/find_pw_ok.html', res_data)

    else:
        return render(request, 'accounts/find_pw.html')


def findpwok(request):
    return render(request, 'accounts/find_pw_ok.html')


def findpwemail(request, email):
    if request.method == "GET":
        def email_auth_num():
            LENGTH = 6
            string_pool = string.digits # 번호만
            certification_number = ""
            for i in range(LENGTH):
                certification_number += random.choice(string_pool)
            return certification_number

        certification_number = email_auth_num()
        data = {
            'email': email,
            'certification_num': certification_number
        }
        message = render_to_string('accounts/pw_change.html',
                                   {
                                       'certification_number': certification_number,
                                   })
        mail_title = "계정 비밀번호 변경 인증번호"
        mail_to = email
        email = EmailMessage(mail_title, message, to=[mail_to])
        email.send()
        print(f"인증번호:{certification_number}, 이메일:{mail_to}, 메일이름:{mail_title}")
        return render(request, 'accounts/find_pw_email.html', data) # data도 같이 보냄.
    return render(request, 'accounts/find_pw_email.html')


def findpwfail(request):
    return render(request, 'accounts/find_pw_fail.html')


def resetpw(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('newPassword', None)

        user = auth_User.objects.get(email=email)

        try:
            user.password = password
            user.save()
            return render(request, 'accounts/login.html')
        except:
            print("")

    return render(request, 'accounts/reset_pw.html')


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
        return render(request, 'main/main.html', {'error': '계정 활성화 오류'})
    return


def mobile_search_iframe(request):
    return render(request, 'accounts/mobile_address_search_iframe.html')
