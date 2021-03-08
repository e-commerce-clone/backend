from django.urls import path
from . import views
from django.views.generic.base import TemplateView
app_name = 'main'

urlpatterns = [
    path('', views.main, name="main"),
    path('mobile_address_search/', views.mobile_address_search, name='mobile_address_search'),
    path('mobile_address_iframe', views.mobile_address_iframe, name='mobile_address_iframe'),
    path('mobile/',
         TemplateView.as_view(template_name='main/main_mobile.html'),
         name='mobile_main'),
]