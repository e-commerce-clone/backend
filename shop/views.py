from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from photo.models import Product_photo
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from cart.views import add_cart
# Create your views here.


def product_detail(request, id):
    if request.method=="POST":
        a=request.POST.get('count')
        print(a)
    product = get_object_or_404(Product, id=id)
    image = get_object_or_404(Product_photo, product=product)
    return render(request, 'shop/product_detail.html', context={'product': product,
                                                                'image': image})


def product_list(request):
    photos = Product_photo.objects.all()
    if request.method == "POST":
        add_cart(request, request.POST.get('product_id'))
    return render(request, 'shop/product_list.html', {'photos': photos})


def mobile_product_list(request):
    photos = Product_photo.objects.all()
    return render(request, 'shop/mobile_product_list.html', {'photos': photos})


def product_review(request):
    return render(request, 'shop/product_review_list.html')


@csrf_exempt
def product_check(request):
    product_name = request.GET.get('product_name')
    context = {'overlap': product_name}
    return JsonResponse(context)


def mobile_category(request):
    return render(request, 'shop/mobile_category.html')

def product_search(request):
    #search_products = None


    if request.method == "GET":
        search_keyword = request.GET.get('search_key', '')
        product_list = Product_photo.objects.order_by('-id')

        search_products = product_list.filter(product__name__icontains=search_keyword)
        print(search_products)
        print(search_keyword)

        return render(request, 'shop/product_search.html', {'photos': search_products})

    elif request.method == "POST":
        add_cart(request, request.POST.get('produc_id'))
        print(request.POST.get('produc_id'))

        return render(request, 'cart/cart.html')

    # elif request.method == "POST":
    #     add_cart(request, request.POST.get('product_id'))
    #     print(request.POST.get('product_id'))

    #print(search_keyword)

    # search_keyword=request.GET.get('search_key', '')
    # product_list=Product_photo.objects.order_by('-id')
    # # page = request.GET.get('page', '1')

    #print(search_products)
    # paginator = Paginator(product_list, 100)                                         # 페이지 나누기
    # page_obj = paginator.get_page(page)
    #return render(request, 'shop/product_search.html', {'photos': search_products})

