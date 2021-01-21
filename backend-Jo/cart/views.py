from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product, Photo
from .models import Cart, CartItem

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    photo = get_object_or_404(Photo, product=product)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += int(request.POST['count'])
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = request.POST['count'],
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
def cart_detail(request, total=0, ship_price=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
            #photos = get_object_or_404(Photo, product=cart_item)
        if total <= 40000:
            ship_price = 3000
            total += ship_price
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart/cart_item.html', dict(cart_items = cart_items, total = total, ship_price = ship_price, photos = photos, counter=counter))
"""
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'],
                                                           'is_update':True})
    return render(request, 'cart/cart.html', {'cart':cart})
"""