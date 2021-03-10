from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomerService, Notice
from accounts.models import Profile
from django.contrib.auth.models import User as auth_User
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.urls import reverse

# Create your views here.





def inquire_list(request): # 사용자 1:1문의 목록 표시
    user = request.user
    iq_list = CustomerService.objects.order_by('-create_date') # 작성일 순으로 데이터 추출
    datas = {
        'iq_list':iq_list,
    }
    # 로그인이 되어있을 경우 -> 문의 목록 페이지로 이동
    if user.is_authenticated:
        return render(request, "customer_service/customer_page.html", datas)

    # login이 안되어있을 경우 -> 로그인 페이지로 이동
    if not user.is_authenticated:
        return render(request, "accounts/login.html")
    
    



def write(request): # 1:1문의 작성
    user = request.user
    try:
        profile = Profile.objects.get(user=user) # 로그인한 정보를 통해 이메일, 전화번호 데이터 추출
        email = profile.email
        phone = profile.phone_number
    except:
        data={
            'admin':1, # 로그인한 정보가 admin일 경우 처리
        }
        return render(request, "customer_service/customer_page.html",data)
    

    if request.method=='POST': # 사용자가 1:1문의 작성 제출했을 경우 - post로 값을 가져옴
        category = request.POST.get('itemcd', None)
        order_num = request.POST.get('ordno', None)
        post_title = request.POST.get('subject', None)
        post_content = request.POST.get('contents', None)
        person_name = profile.person_name
        try:
            image = request.FILES['file[]'] # 미구현 상태
        except: image = "no_image"
        create_date = DateFormat(datetime.now()).format('Y-m-d')
        
        print(category,order_num,post_title,post_content,person_name,image,create_date) # test 콘솔 출력
        
        cs = CustomerService( # 가져온 값들을 db에 저장
            category=category,
            order_num=order_num,
            post_title=post_title,
            post_content=post_content,
            person_name=person_name,
            create_date=create_date,
            image=image)
        
        try:
            cs.save() # db에 반영
        except Exception as e:
            print(e)        
        
        return redirect('/customer_service/customer_page') # 문의 목록 페이지로 이동
    
    

    data = { # 값을 제출하기 전의 경우 - 사용자로 부터 이메일, 전화번호 데이터 추출 후 전달 - 화면에 미리 표시 위함.(readonly)
        'email':email,
        'phone':phone,
    }

    return render(request, "customer_service/customer_write.html",data)
    

def edit(request): # 1:1문의 수정 시 작성 페이지
    
    if request.method=="POST":
        title = request.POST.get('title',None) # 제목은 readonly로 처리
        uid = request.POST.get('user',None)
        print(title,uid)
        user = auth_User.objects.get(username=uid) # 사용자 정보

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
        } # readonly

    return render(request, "customer_service/customer_edit.html",data)

def edit_ok(request): # 1:1문의 수정 완료 후 완료 페이지
    user = request.user
    profile = Profile.objects.get(user=user) # 사용자 정보
    if request.method=="POST": # 사용자가 1:1문의 작성 수정을 완료해서 제출한 경우 - post로 값을 가져옴
        category = request.POST.get('itemcd', None)
        order_num = request.POST.get('ordno', None)
        post_title = request.POST.get('subject', None)
        post_content = request.POST.get('contents', None)
        person_name = profile.person_name
        try:
            image = request.FILES['file[]'] # 미구현
        except: image = "no_image"
        create_date = DateFormat(datetime.now()).format('Y-m-d')
        
        print(category,order_num,post_title,post_content,person_name,image,create_date)
        
        # update query - db 수정
        cs = CustomerService.objects.get(post_title=post_title)
        cs.category = category
        cs.order_num=order_num
        cs.post_content=post_content
        cs.image=image
        cs.create_date=create_date
        try:
            cs.save() # 반영
        except Exception as e:
            print(e)        
        return redirect('/customer_service/customer_page') # 목록 페이지로 이동



def delete(request, pid): # 1:1문의 삭제
    cs = CustomerService.objects.get(id=pid) # 게시물 정보
    cs.delete()    # 삭제 
    return redirect('/customer_service/customer_page') # 목록 페이지로 이동
    

def view_ordno(request): # 주문내역 조회 페이지 - 작은 프레임창에 띄울 것 -- 미완성 : 주문완료 데이터와 연결 필요.
    return render(request, "customer_service/order_content.html") # 현재는 임시로 프론트에서 만든 페이지로 연결된 상태.
     

def notice_list(request): # 공지사항 목록 표시
    nt_list = Notice.objects.order_by('-create_date')
    datas = {
        'list':nt_list,
    }
    return render(request,"customer_service/notice_page.html", datas)
    
        
def notice_details(request, pk): # 공지사항 상세 페이지 - notice_list에서 제목을 클릭했을 때 해당 내용(content)볼 수 있음.
    nt = Notice.objects.get(title=pk) # 공지사항 게시물 정보
    print(nt.title) # test 콘솔 출력
    
    data = { # 공지사항 게시물 정보에서 가져온 값 전달
        'hit':nt.hit,
        'title':nt.title,
        'content':nt.content,
        'person_name':nt.person_name,
        'date':nt.create_date,
    } 
    return render(request,"customer_service/notice_details.html", data)  # 상세 페이지 이동



def write_nt(request): # 공지사항 게시물 작성=등록 (1:1문의와 유사)

    if request.method=='POST':
        category = request.POST.get('itemcd', None)
        hit = 0 # 조회수 미구현
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