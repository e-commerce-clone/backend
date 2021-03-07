from django.db import models
from shop.models import Product
from accounts.models import Profile
from django.contrib.auth.models import User
# Create your models here.


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField('제목', max_length=50)
    contents = models.TextField('내용')
    product_image = models.ImageField('제품 이미지', upload_to="reviews/image/%Y/%m/%d")
    views = models.PositiveIntegerField('조회수', default=0)
    helps = models.PositiveIntegerField('도움이 돼요', default=0)
    created_at = models.DateField('작성 일자', auto_now_add=True)

    def __str__(self):
        return self.title


# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField('수량')
#
#     order_time = models.DateTimeField('주문 시간', auto_now_add=True)
#
#     def __str__(self):
#         return self.product.name


class Delivery(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField('받을 사람', max_length=20, default="", blank=True)
    calling = models.CharField('연락처', max_length=20, default="", blank=True)
    address = models.CharField('배송지', max_length=50)
    delivery_type = models.CharField('배송 유형', max_length=20, null=True)
    basic_address = models.BooleanField('기본 배송지 설정', default=False, null=True)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return self.address

