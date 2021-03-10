from django.urls import path
from . import views

app_name = 'customer_service'

urlpatterns = [
    path('customer_page/', views.inquire_list, name='iq_list'),
    path('customer_write/', views.write, name='iq_write'),
    path('customer_edit/', views.edit, name='iq_edit'),
    path('cutomer_editok/', views.edit_ok, name='edit_ok'),
    path('cutomer_delete/<int:pid>', views.delete, name='delete'),    
    path('notice_page/', views.notice_list, name='nt_list'),
    path('notice_details/<str:pk>', views.notice_details, name='nt_details'),
    path('notice_write/', views.write_nt, name='nt_write'),
    path('', views.view_ordno, name='ordno'),
       
]