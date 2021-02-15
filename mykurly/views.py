from django.shortcuts import render

# Create your views here.


def order_list(request):
    return render(request, 'mykurly/mykurly_order_list.html')


def order_view(request):
    return render(request, 'mykurly/mykurly_orderview.html')


def review(request):
    return render(request, 'mykurly/mykurly_review.html')


def review_register(request):
    return render(request, 'mykurly/mykurly_review_register.html')


def information(request):
    return render(request, 'mykurly/mykurly_information.html')


def information_modify(request):
    return render(request, 'mykurly/mykurly_information_modify.html')


def delivery_list(request):
    return render(request, 'mykurly/mykurly_delivery_list.html')


def delivery_modify(request):
    return render(request, 'mykurly/mykurly_delivery_modify.html')


def address_search(request):
    return render(request, 'mykurly/mykurly_address_search.html')
