from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.CharField('제목', max_length=50)
    contents = models.TextField('내용')
    product_image = models.ImageField('제품 이미지', upload_to="reviews/image/%Y/%m/%d")
    views = models.PositiveIntegerField('조회수')
    helps = models.PositiveIntegerField('도움이 돼요')
    created_at = models.DateTimeField('작성 일자', auto_now_add=True)

    def __str__(self):
        return self.title
