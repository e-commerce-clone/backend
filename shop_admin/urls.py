from django.urls import path
from . import views

app_name = 'shop_admin'

urlpatterns = [
    path('product_manage/', views.prd_manage, name="product_manage"),
    path('product_manage/', views.prd_manage, name="product_manage_re"),
    path('product_manage/product_modify/<int:id>/', views.prd_modify, name="product_modify"),
    path('product_manage/product_upload/', views.prd_upload, name="product_upload"),
    path('product_manage/product_order/', views.prd_order, name="product_order"),
    path('product_manage/product_upload/product_manual/', views.prd_manual, name="product_manual"),
]