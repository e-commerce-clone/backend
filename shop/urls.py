from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('product_list/<str:main_category>/', views.product_list, name='product_list'),
    path('product_list/<str:main_category>/<str:sub_category>/', views.product_in_category, name='product_in_category'),
    path('mobile_product_list/', views.mobile_product_list, name='mobile_product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product_review_list/<int:pk>/', views.product_review_list, name='product_review'),
    path('product_list/product_check', views.product_check, name="product_check"),
    path('mobile_product_list/mobile_category/', views.mobile_category, name='mobile_category'),
    path('product_search/', views.product_search, name='product_search'),
]