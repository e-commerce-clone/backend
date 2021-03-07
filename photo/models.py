from django.db import models
from shop.models import Product
from mykurly.models import Review
# Create your models here.


class Product_photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    main_image = models.ImageField('메인 이미지', upload_to='products/mainImage/%Y/%m/%d')
    sub_image = models.ImageField('서브 이미지', upload_to='products/subImage/%Y/%m/%d')

    class Meta:
        ordering = ['product']
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

    def __str__(self):
        return self.product.name


class Review_photo(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=False)
    image = models.ImageField('제품 이미지', upload_to='reviews/image/%Y/%m/%d')

    class Meta:
        ordering = ['review']
        verbose_name = 'review_photo'
        verbose_name_plural = 'review_photos'

    def __str__(self):
        return self.review.name
