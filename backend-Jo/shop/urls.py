from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'shop'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('mobile_product_list/', views.mobile_product_list, name='mobile_product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product_review_list.html', TemplateView.as_view(template_name='product_review_list.html'),
         name='product_review'),
    path('product_list/product_check', views.product_check, name="product_check"),
    path('mobile_product_list/mobile_category/', views.mobile_category, name='mobile_category'),
]