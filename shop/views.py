from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from photo.models import Product_photo
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    image = get_object_or_404(Product_photo, product=product)
    return render(request, 'shop/product_detail.html', context={'product': product,
                                                                'image': image})


def product_list(request):
    photos = Product_photo.objects.all()
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
