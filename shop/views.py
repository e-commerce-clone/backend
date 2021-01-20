from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Photo
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    image = get_object_or_404(Photo, product=product)
    return render(request, 'shop/product_detail.html', context={'product': product,
                                                                'image': image})


def product_list(request):
    products = Product.objects.all()
    photos = Photo.objects.all()
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