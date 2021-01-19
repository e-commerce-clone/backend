from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('', views.main, name='main'),
    path('shop_admin/', views.product_join, name='product_join'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]