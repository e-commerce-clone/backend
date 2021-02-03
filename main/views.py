from django.shortcuts import render
# Create your views here.


def main(request):
    return render(request, 'main/main.html')


def mobile_address_search(request):
    return render(request, 'main/mobile_address_search.html')


def mobile_address_iframe(request):
    return render(request, 'main/mobile_address_iframe.html')