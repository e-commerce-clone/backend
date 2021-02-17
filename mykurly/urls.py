from django.urls import path
from . import views

app_name = 'mykurly'

urlpatterns = [
    path('order_list/', views.order_list, name="order_list"),
    path('order_list/detail/', views.order_view, name="order_view"),
    path('delivery_list/', views.delivery_list, name="delivery_list"),
    path('delivery_list/modify/', views.delivery_modify, name="delivery_modify"),
    path('delivery_list/address_search/', views.address_search, name="address_search"),
    path('review/', views.review, name="review"),
    path('review_register/<str:username>/<int:pk>/', views.review_register, name="review_register"),
    path('information/', views.information, name="information"),
    path('information/modify/<int:pk>/', views.information_modify, name="information_modify"),
    path('information/withdrawal/<int:pk>/', views.withdrawal, name="withdrawal"),
]