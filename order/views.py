from django.shortcuts import render, get_list_or_404, redirect, reverse
from accounts.models import Profile
from shop.models import Product
from photo.models import Product_photo
from mykurly.models import Delivery
from cart.models import CartItem, Cart
from .models import Order_item, Order
from django.contrib.auth.models import User as auth_User
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def order(request):
    if request.method == "GET":
        pk = request.user.pk

        user = auth_User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)

        cart = Cart.objects.get(cart_id=profile.cart_key)
        cart_items = CartItem.objects.filter(cart=cart)

        delivery = Delivery.objects.get(profile=profile, basic_address=True)

        context = {
            'profile': profile,
            'cart_items': cart_items,
            'delivery': delivery
        }

        return render(request, 'order/order.html', context)

    elif request.method == "POST":
        e_money = request.POST.get("using_point", 0)
        if not e_money:
            e_money = "0"
        total_price = request.POST.get("product_price_value")
        return redirect(reverse('kakaopay:index') + f"?e_money={e_money}&total_price={total_price}")

