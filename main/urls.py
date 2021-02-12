from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name="main"),
    path('mobile_address_search/', views.mobile_address_search, name='mobile_address_search'),
    path('mobile_address_iframe', views.mobile_address_iframe, name='mobile_address_iframe'),
]