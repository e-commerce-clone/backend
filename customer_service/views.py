from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomerService, Notice
from accounts.models import Profile
from django.contrib.auth.models import User as auth_User
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.urls import reverse

# 로그인 시 작성자 이름을 어케 가져올까.
# Create your views here.





def inquire_list(request): # 문의 목록 표시
    user = request.user
    iq_list = CustomerService.objects.order_by('-create_date')
    value=0
    datas = {
        'iq_list':iq_list,
        'value':value,
    }
    # 로그인 세션이 존재할 경우 post로 받아온 값이 있을 경우
    # 번호(key) 카테고리 제목 작성자(forienkey) 작성일을 
    # customer_page.html에 표시
    if user.is_authenticated:
        return render(request, "customer_service/customer_page.html", datas)
        
    if not user.is_authenticated:
        return render(request, "accounts/login.html")
        # login이 안되어있을 경우 -> 로그인 페이지로 이동
    
    



def write(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        email = profile.email
        phone = profile.phone_number
    except:
        data={
            'admin':1,
        }
        return render(request, "customer_service/customer_page.html",data)
    

    if request.method=='POST':
        category = request.POST.get('itemcd', None)
        order_num = request.POST.get('ordno', None)
        post_title = request.POST.get('subject', None)
        post_content = request.POST.get('contents', None)
        person_name = profile.person_name
        try:
            image = request.FILES['file[]']
        except: image = "no_image"
        create_date = DateFormat(datetime.now()).format('Y-m-d')
        
        print(category,order_num,post_title,post_content,person_name,image,create_date)
        
        cs = CustomerService(
            category=category,
            order_num=order_num,
            post_title=post_title,
            post_content=post_content,
            person_name=person_name,
            create_date=create_date,
            image=image)
        
        try:
            cs.save()
        except Exception as e:
            print(e)        
        
        # return render(request, 'customer_service/customer_page.html', datas)
        return redirect('/customer_service/customer_page')
    # (post)
    # 글쓰기 페이지로 부터 post로 받아온 값이 있을 경우
    # db로 전달 후
    # inquire_list로 연결 (alert창:문의가 접수되었습니다.)
    

    data = {
        'email':email,
        'phone':phone,
    }

    return render(request, "customer_service/customer_write.html",data)
    

def edit(request):
    
    if request.method=="POST":
        title = request.POST.get('title',None)
        uid = request.POST.get('user',None)
        print(title,uid)
        user = auth_User.objects.get(username=uid)

        try:
            profile = Profile.objects.get(user=user)
        except:
            print("no user info")
        email = profile.email
        phone = profile.phone_number
        data = {
            'title':title,
            'email':email,
            'phone':phone,
        }

    return render(request, "customer_service/customer_edit.html",data)

def edit_ok(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method=="POST":
        category = request.POST.get('itemcd', None)
        order_num = request.POST.get('ordno', None)
        post_title = request.POST.get('subject', None)
        post_content = request.POST.get('contents', None)
        person_name = profile.person_name
        try:
            image = request.FILES['file[]']
        except: image = "no_image"
        create_date = DateFormat(datetime.now()).format('Y-m-d')
        
        print(category,order_num,post_title,post_content,person_name,image,create_date)
        
        # update query
        cs = CustomerService.objects.get(post_title=post_title)
        cs.category = category
        cs.order_num=order_num
        cs.post_content=post_content
        cs.image=image
        cs.create_date=create_date
        try:
            cs.save()
        except Exception as e:
            print(e)        
        return redirect('/customer_service/customer_page')



def delete(request, pid):
    cs = CustomerService.objects.get(id=pid)
    cs.delete()    
    return redirect('/customer_service/customer_page')
    

def view_ordno(request):
    return render(request, "customer_service/order_content.html")




# def answer(request):
#     # 관리자가 문의답변을 했을 경우 db를 반영함.
#     # 그렇지 않을 경우 1문의답변이없는경우 템플릿을 보임.
     

def notice_list(request): # 문의 목록 표시
    nt_list = Notice.objects.order_by('-create_date')
    datas = {
        'list':nt_list,
    }
    return render(request,"customer_service/notice_page.html", datas)
    # login이 안되어있을 경우 -> 로그인 페이지로 이동
    # 공지사항 리스트
        
def notice_details(request, pk):
    nt = Notice.objects.get(title=pk)
    print(nt.title)
    
    data = {
        'hit':nt.hit,
        'title':nt.title,
        'content':nt.content,
        'person_name':nt.person_name,
        'date':nt.create_date,
    }
    return render(request,"customer_service/notice_details.html", data)
#     # notice_list에서 제목을 클릭했을 때 해당 내용(content)볼 수 있음.

def write_nt(request):

    if request.method=='POST':
        category = request.POST.get('itemcd', None)
        hit = 0
        title = request.POST.get('subject', None)
        content = request.POST.get('contents', None)
        person_name = '관리자'
        create_date = DateFormat(datetime.now()).format('Y-m-d')
        
        print(category,hit,title,content,person_name,create_date)
        
        nt = Notice(
            category=category,
            hit=hit,
            title=title,
            content=content,
            person_name=person_name,
            create_date=create_date,
            )
        
        try:
            nt.save()
        except Exception as e:
            print(e)        
        
        return redirect('/customer_service/notice_page')
    return render(request, "customer_service/notice_write.html")