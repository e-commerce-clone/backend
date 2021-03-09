from django.urls import path
from . import views

app_name = 'kakaopay'

urlpatterns = [
    path('', views.index, name='index'),
    path('payApproval/', views.payApproval, name='payApproval'),
    path('payCancel/', views.payCancel, name='payCancel'),
    path('payFail/', views.payFail, name='payFail'),
]