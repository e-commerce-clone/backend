from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product_search/',views.product_search, name='product_search'),
]