from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Product, Category, Photo
from cart.views import _cart_id,add_cart
from cart.models import Cart

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


def product_detail(request, id):
    if request.method=="POST":
        a=request.POST.get('count')
        print(a)
    product = get_object_or_404(Product, id=id)
    image = get_object_or_404(Photo, product=product)
    return render(request, 'shop/product_detail.html', context={'product': product,
                                                                'image': image})


def product_list(request):

    products = Product.objects.all()
    photos = Photo.objects.all()
    if request.method == "POST":
        add_cart(request, request.POST.get('product_id'))
    return render(request, 'shop/product_list.html', {'photos': photos})


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category)
        products = products.filter(category=current_category)
    return render(request, 'shop/product_list.html', {
        'current_category': current_category,
        'categories': categories,
        'products': products})

def product_search(request):
    search_keyword=request.GET.get('search_key', '')
    product_list=Photo.objects.order_by('-id')
    # page = request.GET.get('page', '1')

    if search_keyword :
        search_products = product_list.filter(product__name__icontains=search_keyword)

    print(search_products)
    # paginator = Paginator(product_list, 100)                                         # 페이지 나누기
    # page_obj = paginator.get_page(page)
    return render(request, 'shop/product_search.html', {'photos': search_products})

