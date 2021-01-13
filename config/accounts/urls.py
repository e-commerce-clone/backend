from django.urls import path
from .views import register, login, id_overlap_check, email_overlap_check
from . import views
app_name = 'accounts'

urlpatterns = [
     path('login/',
         login,
         name='login'),
     path('',views.logout,name='logout'),
     path('register/',
         register,
         name="register"),
     path('register/id_check',
         id_overlap_check,
         name="id_overlap_check"),
     path('register/email_check',
         email_overlap_check,
         name="email_overlap_check"),
     path('find_id/', views.findid, name='findid'),
     path('find_id_ok/', views.findidok, name="findidok"),
     path('find_id_fail/', views.findidfail, name="findidfail"),
     
     path('find_pw/', views.findpw, name='findpw'),
     path('find_pw_ok/', views.findpwok, name='findpwok'),
     path('find_pw_email/<str:email>/', views.findpwemail, name='findpwemail'),     
     path('find_pw_fail/', views.findpwfail, name="findpwfail"),
     path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
     
     path('reset_pw/', views.resetpw, name="resetpw"),

]
