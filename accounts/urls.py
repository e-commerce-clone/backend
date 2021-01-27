from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name="signup"),
    path('signup/id_check', views.id_overlap_check, name="id_overlap_check"),
    path('signup/email_check', views.email_overlap_check, name="email_overlap_check"),
    path('find_id/', views.findid, name='findid'),
    path('find_id_ok/', views.findidok, name="findidok"),
    # path('find_id_fail/', views.findidfail, name="findidfail"),
    path('find_pw/', views.findpw, name='findpw'),
    path('find_pw_ok/', views.findpwok, name='findpwok'),
    path('find_pw_email/<str:email>/', views.findpwemail, name='findpwemail'),
    # path('find_pw_fail/', views.findpwfail, name="findpwfail"),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('reset_pw/', views.resetpw, name="resetpw"),
]
