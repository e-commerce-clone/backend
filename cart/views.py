from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product
from photo.models import Product_photo
from .models import Cart, CartItem, Profile

@login_required
def _cart_id(request):

    profile = Profile.objects.get(user=request.user)
    cart = profile.cart_key

    if not cart:
        cart = request.session.session_key
        profile.cart_key = cart
        profile.save()

    return cart

@login_required
def add_cart(request):            # image_id
    if request.method == "GET":
        photo = Product_photo.objects.get(id=int(request.GET.get('product_id')))  #id=image_id
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
            cart.save()

        try:
            cart_item = CartItem.objects.get(photo=photo, cart=cart)
            cart_item.quantity += int(request.GET.get('count'))
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                photo=photo,
                quantity=int(request.GET.get('count')),
                cart=cart
            )
            cart_item.save()

        return redirect(request.GET.get('current_url'))

    if request.method == "POST":
        photo = Product_photo.objects.get(id=int(request.POST.get('product_id')))  # id=image_id
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
                photo=photo,
                quantity=int(request.POST.get('count')),
                cart=cart
            )
            cart_item.save()

        return redirect(request.POST.get('current_url'))


@login_required
def add_product(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = Product_photo.objects.get(id=product_id)  # id=image_id
    cart_item = CartItem.objects.get(cart=cart, photo=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart_detail')

@login_required
def decrease_product(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = Product_photo.objects.get(id=product_id)  # id=image_id
    cart_item = CartItem.objects.get(cart=cart, photo=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart_detail')

def delete_product(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = Product_photo.objects.get(id=product_id)  # id=image_id
    cart_item = CartItem.objects.get(cart=cart, photo=product)

    cart_item.delete()

    return redirect('cart:cart_detail')

@login_required
def cart_detail(request, total=0, ship_price=0, payment_amount=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for cart_item in cart_items:
            total += (cart_item.photo.product.price * cart_item.quantity)
            counter += 1

        if total < 40000:
            ship_price = 3000

        payment_amount = total + ship_price
    except ObjectDoesNotExist:
        pass


    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, ship_price=ship_price,
                                                       payment_amount=payment_amount, counter=counter))

def cart_clear(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart.delete()

    return redirect('cart:cart_detail')

def ship_destination(request):
    return render(request, 'cart/ship_destination.html')                                # 미완성


def add_mydestination(request):
    return render(request, 'cart/add_mydestination.html')                               # 미완성
