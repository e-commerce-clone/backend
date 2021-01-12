from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name="signup"),
    path('signup/id_check', views.id_overlap_check, name="id_overlap_check"),
    path('signup/email_check', views.email_overlap_check, name="email_overlap_check"),
    path('find_id/', views.find_id, name="find_id"),
    path('find_pw/', views.find_pw, name="find_pw"),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]
