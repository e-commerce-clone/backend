from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:image_id>/', views.add_cart, name='add_cart'),
    # path('remove/<product_id>/', remove, name='product_remove'),
    path('ship_destination/', views.ship_destination, name='ship_destination'),
    path('add_mydestination', views.add_mydestination, name='add_mydestination'),
]