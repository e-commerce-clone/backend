from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from accounts.models import Profile
from shop.models import Product
from photo.models import Product_photo
from mykurly.models import Delivery
from cart.models import CartItem, Cart
from order.models import Order_item, Order
from django.contrib.auth.models import User as auth_User
import requests
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": f'KakaoAK ' + 'df530ab3e101768ce0adb6e163be98e9',  # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }

        pk = request.user.pk
        e_money = request.GET.get("e_money", 0)
        total_price = request.GET.get("total_price")
        user = auth_User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)

        cart = Cart.objects.get(cart_id=profile.cart_key)
        cart_items = get_list_or_404(CartItem, cart=cart)

        count = len(cart_items)

        if count == 1:
            item_name = cart_items[0].photo.product.name
        else:
            item_name = f"{cart_items[0].photo.product.name} 외 {count - 1}개"

        data = {
            "cid": "TC0ONETIME",  # 테스트용 코드
            "partner_order_id": "1001",  # 주문번호
            "partner_user_id": request.user.username,  # 유저 아이디
            "item_name": item_name,  # 구매 물품 이름
            "quantity": f"{count}",  # 구매 물품 수량
            "total_amount": f"{total_price}",  # 구매 물품 가격
            "tax_free_amount": "0",  # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/kakaopay/payApproval/" + f"?e_money={e_money}&price={total_price}",
            "cancel_url": "http://127.0.0.1:8000/kakaopay/payCancel/",
            "fail_url": "http://127.0.0.1:8000/kakaopay/payFail/",
        }

        res = requests.post(URL, data=data, headers=headers)

        result = res.json()

        request.session['tid'] = result['tid']  # 결제 승인시 사용할 tid를 세션에 저장
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

    pk = request.user.pk
    e_money = request.GET.get("e_money", None)
    price = request.GET.get("price")

    user = auth_User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)

    cart = Cart.objects.get(cart_id=profile.cart_key)
    cart_items = get_list_or_404(CartItem, cart=cart)
    count = len(cart_items)

    if count == 1:
        item_name = cart_items[0].photo.product.name
    else:
        item_name = f"{cart_items[0].photo.product.name} 외 {count - 1}개"

    total_product_price = 0
    for item in cart_items:
        total_product_price += item.photo.product.price * item.quantity

    order = Order(profile=profile, total_price=price, total_product_price=total_product_price, name=item_name)
    order.save()

    for item in cart_items:
        order_item = Order_item(order=order, product=item.photo, quantity=item.quantity)
        order_item.save()

    profile.e_money = profile.e_money - int(e_money)
    profile.save()

    order_items = get_list_or_404(Order_item, order=order)
    delivery = get_object_or_404(Delivery, profile=profile, basic_address=True)

    context = {
        'res': res,
        'amount': amount,
        'order_items': order_items,
        'delivery': delivery,
        'order': order,
        'e_money': e_money,
    }

    return render(request, 'kakaopay/paySuccess.html', context)


def payFail(request):
    return render(request, 'kakaopay/payFail.html')


def payCancel(request):
    return render(request, 'kakaopay/payCancel.html')
