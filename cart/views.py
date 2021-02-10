from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product
from photo.models import Product_photo
from .models import Cart, CartItem


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, image_id):
    photo = Product_photo.objects.get(id=image_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(photo=photo, cart=cart)
        cart_item.quantity += int(request.POST.get('count'))
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            photo = photo,
            quantity = int(request.POST.get('count')),
            cart = cart
        )
        cart_item.save()

    return redirect('cart:cart_detail')
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # 클라이언트 -> 서버로 데이터 전달
    # 유효성 검사 폼에서 해줌
    form = AddProductForm(request.POST)

    if form.is_vaild():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('cart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')
"""


def cart_detail(request, total=0, ship_price=3000, payment_amount=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.photo.product.price * cart_item.quantity)
            counter += cart_item.quantity
        if counter == 0:
            ship_price = 0
        elif total >= 40000:
            ship_price = 0
        payment_amount = total + ship_price
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, ship_price=ship_price,
                                                  payment_amount=payment_amount, counter=counter))


def ship_destination(request):
    return render(request, 'cart/ship_destination.html')                #미완성


def add_mydestination(request):
    return render(request, 'cart/add_mydestination.html')               #미완성



def sel_addr(request): # +bo0
    return render(request, 'cart/sel_addr.html')