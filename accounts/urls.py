from django.urls import path
from .views import register, login, id_overlap_check, email_overlap_check
app_name = 'accounts'

urlpatterns = [
    path('login/',
         login,
         name='login'),
    path('register/',
         register,
         name="register"),
    path('register/id_check',
         id_overlap_check,
         name="id_overlap_check"),
    path('register/email_check',
         email_overlap_check,
         name="email_overlap_check"),
]
