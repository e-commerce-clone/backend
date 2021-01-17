from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                default="")
    email = models.EmailField('이메일', max_length=30, default="")
    person_name = models.CharField('성명', max_length=20)
    age = models.IntegerField('나이', null=True, editable=False)
    phone_number = models.CharField('전화번호', max_length=20)
    home_address = models.CharField('주소', max_length=100, null=True, blank=True)
    birthday = models.DateField('생년월일', null=True, blank=True)
    created_at = models.DateTimeField('생성 일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정 일자', auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "Profile"

    objects = models.Manager()  # 자동완성 .objects 를 사용하기 위한 설정
