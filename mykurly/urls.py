from django.urls import path
from . import views
from django.views.generic.base import TemplateView
app_name = 'mykurly'

urlpatterns = [
    path('order_list/', views.order_list, name="order_list"),
    path('order_list/detail/', views.order_view, name="order_view"),
    path('delivery_list/<int:pk>/', views.delivery_list, name="delivery_list"),
    path('delivery_list/modify/<int:delivery_pk>', views.delivery_modify, name="delivery_modify"),
    path('delivery_list/<int:pk>/address_search/', views.address_search, name="address_search"),
    path('review/', views.review, name="review"),
    path('review_register/<str:username>/<int:pk>/', views.review_register, name="review_register"),
    path('information/', views.information, name="information"),
    path('information/modify/<int:pk>/', views.information_modify, name="information_modify"),
    path('information/withdrawal/<int:pk>/', views.withdrawal, name="withdrawal"),
    path('mobile_delivery/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_destination.html'),
         name='mobile_delivery'),
    path('mobile_delivery/modify/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_destination_modify.html'),
         name='mobile_delivery_modify'),
    path('mobile_information/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_information.html'),
         name='mobile_information'),
    path('mobile_information/modify/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_information_modify.html'),
         name='mobile_information_modify'),
    path('mobile_order/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_orderlist.html'),
         name='mobile_order'),
    path('mobile_order/detail/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_orderview.html'),
         name='mobile_order_view'),
    path('mobile_review_after/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_review_after.html'),
         name='mobile_review_after'),
    path('mobile_review_before/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_review_before.html'),
         name='mobile_review_before'),
    path('mobile_review_detail/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_review_detail.html'),
         name='mobile_review_detail'),
    path('mobile_review_register/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_review_register.html'),
         name='mobile_review_register'),
    path('mobile_withdrawal/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_withdrawal.html'),
         name='mobile_withdrawal'),
    path('mobile_emoneylist/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_emoneylist.html'),
         name='mobile_emoneylist'),
    path('mobile_menulist/',
         TemplateView.as_view(template_name='mykurly/mobile_mykurly_menulist.html'),
         name='mobile_menulist'),
]
