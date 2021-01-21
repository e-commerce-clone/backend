from django.urls import path
from . import views

app_name='cart'

urlpatterns= [
    path('', views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    #path('remove/<product_id>/', remove, name='product_remove'),
]