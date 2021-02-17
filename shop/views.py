from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category, MainCategory
from mykurly.models import Review
from photo.models import Product_photo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import math
from urllib import parse
from cart.views import add_cart

# Create your views here.


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    image = get_object_or_404(Product_photo, product=product)
    return render(request, 'shop/product_detail.html', context={'product': product,
                                                                'image': image})


def product_list(request, main_category):
    if request.method == "POST":
        add_cart(request, request.POST.get('product_id'))
    page = int(request.GET.get('page', 1))                  # 현재 페이지 번호를 가져온다. 없으면 1을 가져온다.
    paginated_by = 3                                        # 페이지당 노출될 개수

    m_category = get_object_or_404(MainCategory, name=main_category)
    all_categories = get_list_or_404(Category, main_category=m_category)

    photos = []
    products_in_category = []
    for s_category in all_categories:
        tmp = get_list_or_404(Product, category=s_category)
        for product in tmp:
            products_in_category.append(product)
    for product in products_in_category:
        photos.append(get_object_or_404(Product_photo, product=product))
    total_count = len(photos)

    if paginated_by >= total_count:
        total_page = 1
    else:
        total_page = math.ceil(total_count / paginated_by)

    page_range = range(1, total_page+1)

    start_index = paginated_by * (page - 1)
    end_index = paginated_by * page
    photos = photos[start_index:end_index]
    category_name = None

    return render(request, 'shop/product_list.html', {'photos': photos, 'total_page': total_page,
                                                      'page_range': page_range, 'categories': all_categories,
                                                      'category_name': category_name, 'main_category': main_category})


def product_in_category(request, main_category, sub_category):
    if request.method == "POST":
        add_cart(request, request.POST.get('product_id'))
    page = int(request.GET.get('page', 1))              # 현재 페이지 번호를 가져온다. 없으면 1을 가져온다.
    category_name = sub_category                        # 카테고리 이름을 가져온다.
    paginated_by = 3                                    # 페이지당 노출될 개수

    if category_name == "all":
        photos = get_list_or_404(Product_photo)
    else:
        category = get_object_or_404(Category, name=category_name)
        products = get_list_or_404(Product, category=category)
        photos = []
        for product in products:
            photos.append(get_object_or_404(Product_photo, product=product))

    total_count = len(photos)

    if paginated_by >= total_count:
        total_page = 1
    else:
        total_page = math.ceil(total_count / paginated_by)

    page_range = range(1, total_page + 1)

    m_category = get_object_or_404(MainCategory, name=main_category)
    all_categories = get_list_or_404(Category, main_category=m_category)

    start_index = paginated_by * (page - 1)
    end_index = paginated_by * page
    photos = photos[start_index:end_index]
    return render(request, 'shop/product_list.html', {'photos': photos, 'total_page': total_page,
                                                      'page_range': page_range, 'categories': all_categories,
                                                      'category_name': category_name, 'main_category': main_category})



def mobile_product_list(request):
    photos = Product_photo.objects.all()
    return render(request, 'shop/mobile_product_list.html', {'photos': photos})


def product_review_list(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    count = 0
    for _ in reviews:
        count += 1
    counts = list(range(1, count + 1))
    data = {
        'reviews': reviews,
        'pk': pk,
        'counts': counts
    }
    return render(request, 'shop/product_review_list.html', data)


@csrf_exempt
def product_check(request):
    product_name = request.GET.get('product_name')
    context = {'overlap': product_name}
    return JsonResponse(context)


def mobile_category(request):
    return render(request, 'shop/mobile_category.html')
