from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from shop.models import Product, Category, Photo
from django.urls import reverse
from django.views.generic.edit import DeleteView
# Create your views here.


def prd_manage(request):
    if request.method == "GET":
        products = Product.objects.all()
    elif request.method == "POST":
        product = Product.objects.get(pk=request.POST.get('delete'))
        product.delete()
        return HttpResponseRedirect(reverse('shop_admin:product_manage_re'))
    return render(request, 'shop_admin/admin_page_prd_manage.html', {'products': products})


def prd_modify(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop_admin/admin_page_prd_modify.html', context={'product': product})


def prd_upload(request):
    if request.method == "POST":
        name = request.POST.get('product_name', None)
        one_description = request.POST.get('product_introduce', None)
        price = request.POST.get('product_price', None)
        sales_unit = request.POST.get('product_unit', None)
        stock = request.POST.get('product_count', None)
        weight = request.POST.get('product_weight', None)
        delivery = request.POST.get('product_delivery', None)
        origin = request.POST.get('product_origin', None)
        packing_type = request.POST.get('product_packing', None)
        shelf_life = request.POST.get('product_life', None)
        guide = request.POST.get('product_information', None)
        description = request.POST.get('product_description', None)
        try:
            main_image = request.FILES['product_main_image']
        except:
            main_image = "products/no_image.png"

        try:
            sub_image = request.FILES['product_sub_image']
        except:
            sub_image = "products/no_image.png"

        category = Category(name=request.POST.get('product_category', None))
        category.save()

        product = Product(
            name=name,
            one_description=one_description,
            description=description,
            price=price,
            sales_unit=sales_unit,
            stock=stock,
            weight=weight,
            delivery=delivery,
            origin=origin,
            packing_type=packing_type,
            shelf_life=shelf_life,
            guide=guide,
            category=category
        )
        product.save()
        photo = Photo(product=product, main_image=main_image, sub_image=sub_image)
        photo.save()

        return redirect(reverse('shop_admin:product_manage'))
    return render(request, 'shop_admin/admin_page_prd_upload.html')


def prd_order(request):
    return render(request, 'shop_admin/admin_page_prd_order_manage.html')


def prd_manual(request):
    return render(request, 'shop_admin/product_manual.html')

