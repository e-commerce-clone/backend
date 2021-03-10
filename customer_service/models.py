from django.db import models
from django.conf import settings
from accounts.models import Profile

# Create your models here.


class CustomerService(models.Model):
    category = models.CharField(verbose_name='카테고리', max_length=10, default="")
    order_num = models.CharField(verbose_name='주문번호', max_length=20)
    post_title = models.CharField(verbose_name='제목', max_length=20, default="")
    post_content = models.TextField(verbose_name='내용', max_length=250, default="")
    person_name = models.CharField(verbose_name='작성자', max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    answer=models.CharField(verbose_name='답변', max_length=100, default="")

    def __str__(self):
        return self.post_title # 데이터 조회 시 제목을 보여줌.

    class Meta:
        db_table = "CustomerService"

    objects = models.Manager()  # 자동완성 .objects 를 사용하기 위한 설정

class Notice(models.Model):
    category = models.CharField(verbose_name='분류', max_length=10, default="")
    hit = models.PositiveIntegerField(verbose_name='조회수', default=0)
    title = models.CharField(verbose_name='제목', max_length=20, default="")
    content = models.TextField(verbose_name='내용', max_length=250, default="")
    person_name = models.CharField(verbose_name='작성자', max_length=20)
    create_date = models.DateTimeField(verbose_name='작성일', auto_now_add=True)

    def __str__(self):
        return self.title # 데이터 조회 시 제목을 보여줌.

    class Meta:
        db_table = "Notice"
    
    @property
    def update_counter(self):
        self.hit = self.hit+1
        self.save()

