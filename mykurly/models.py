from django.db import models
from shop.models import Product
from accounts.models import Profile
# Create your models here.


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    title = models.CharField('제목', max_length=50)
    contents = models.TextField('내용')
    product_image = models.ImageField('제품 이미지', upload_to="reviews/image/%Y/%m/%d")
    views = models.PositiveIntegerField('조회수', default=0)
    helps = models.PositiveIntegerField('도움이 돼요', default=0)
    created_at = models.DateField('작성 일자', auto_now_add=True)
    count = models.PositiveIntegerField('번호', default=1)

    def __str__(self):
        return self.title
