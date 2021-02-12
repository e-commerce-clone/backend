from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests


@login_required
def index(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": f'KakaoAK ' + 'df530ab3e101768ce0adb6e163be98e9',    # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",   # 변경불가
        }
        data = {
            "cid": "TC0ONETIME",  # 테스트용 코드
            "partner_order_id": "1001",  # 주문번호
            "partner_user_id": request.user.username,  # 유저 아이디
            "item_name": "고구마",  # 구매 물품 이름
            "quantity": "1",  # 구매 물품 수량
            "total_amount": "12000",  # 구매 물품 가격
            "tax_free_amount": "0",  # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/kakaopay/payApproval/",
            "cancel_url": "http://127.0.0.1:8000/kakaopay/payCancel/",
            "fail_url": "http://127.0.0.1:8000/kakaopay/payFail/",
        }

        res = requests.post(URL, data=data, headers=headers)

        result = res.json()

        request.session['tid'] = result['tid']     # 결제 승인시 사용할 tid를 세션에 저장
        next_url = result['next_redirect_pc_url']  # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

    return render(request, 'kakaopay/index.html')


def payApproval(request):
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "df530ab3e101768ce0adb6e163be98e9",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    data = {
        "cid": "TC0ONETIME",  # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",  # 주문번호
        "partner_user_id": request.user.username,  # 유저 아이디
        "pg_token": request.GET.get("pg_token"),  # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, data=data, headers=headers)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'kakaopay/paySuccess.html', context)

def payFail(request):
    return render(request, 'kakaopay/payFail.html')

def payCancel(request):
    return render(request, 'kakaopay/payCancel.html')