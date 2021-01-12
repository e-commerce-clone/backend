from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


def main(request):
    return render(request, 'shop/main.html')


def product_join(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        description = request.POST.get('introduction', None)
        price = request.POST.get('price', None)
        sales_unit = request.POST.get('unit', None)
        weight = request.POST.get('weight', None)
        delivery = request.POST.get('delivery', None)
        origin = request.POST.get('origin', None)
        packing_type = request.POST.get('packing', None)
        shelf_life = request.POST.get('life', None)
        category = Category(name=request.POST.get('category', None))
        category.save()
        product = Product(
            name=name,
            description=description,
            price=price,
            sales_unit=sales_unit,
            weight=weight,
            delivery=delivery,
            origin=origin,
            packing_type=packing_type,
            shelf_life=shelf_life,
            category=category
        )
        product.save()
        return render(request, "shop/main.html")

    return render(request, "shop/shop_admin.html")


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', context={'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


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
