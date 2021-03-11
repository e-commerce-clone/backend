from django.urls import path
from . import views

app_name='cart'

urlpatterns= [
    path('', views.cart_detail,name='cart_detail'),
    path('add/', views.add_cart, name='add_cart'),
    # path('remove/<product_id>/', remove, name='product_remove'),
    path('ship_destination/', views.ship_destination, name='ship_destination'),
    path('add_mydestination/', views.add_mydestination, name='add_mydestination'),
    path('add/<int:product_id>', views.add_product, name='add_product'),
    path('decrease/<int:product_id>/', views.decrease_product, name='decrease_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('sel_addr', views.sel_addr, name='sel_addr'), # 메인화면 부분.
    path('clear/', views.cart_clear, name='cart_clear')
]