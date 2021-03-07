from django.db import models
from accounts.models import Profile
from shop.models import Product
from photo.models import Product_photo
# Create your models here.


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField('주문 상품 이름', max_length=100)
    total_price = models.PositiveIntegerField('총 결제 금액', null=True, default=0)
    total_product_price = models.PositiveIntegerField('총 상품 금액', null=True, default=0)
    order_time = models.DateTimeField('주문 시간', auto_now_add=True)
    order_type = models.CharField('주문상태', max_length=100, default="결제완료")

    def __str__(self):
        return self.profile.user.username


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_type = models.CharField('주문상태', max_length=100, default="결제완료")
    product = models.ForeignKey(Product_photo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('수량')

    def __str__(self):
        return self.product.product.name
