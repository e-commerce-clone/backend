from django.db import models
from django.urls import reverse
# Create your models here.


class MainCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'main_category'
        verbose_name_plural = 'main_categories'

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.SET_NULL,
                                      null=True)
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)         # 검색엔진에 노출되게 하기위한 필드
    """
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, allow_unicode=True)
    """

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list', args=[self.id])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='products')
    # on_delete => 카테고리가 지워지면 제품을 그대로 유지하고 category 값을 null 로 바꿈
    name = models.CharField('제품명', max_length=200, db_index=True, null=True)
    """
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, allow_unicode=True)
    """
    # allow_unicode => 한글을 사용하기 위한 옵션
    sales_unit = models.CharField('판매단위', max_length=10, null=True)
    weight = models.CharField('중량/용량', max_length=10, null=True)
    delivery = models.CharField('배송구분', max_length=200, null=True)
    one_description = models.CharField('한줄설명', max_length=150, blank=True)
    origin = models.CharField('원산지', max_length=50, null=True)
    packing_type = models.CharField('포장타입', max_length=50, null=True)
    guide = models.CharField('안내사항', max_length=200, null=True)
    shelf_life = models.CharField('유통기한', max_length=200, null=True)
    description = models.TextField('상품설명', blank=True)
    price = models.DecimalField('가격', max_digits=10, decimal_places=0, null=True)
    stock = models.PositiveIntegerField('재고', null=True)                    # 재고
    available_display = models.BooleanField('판매가능여부', default=True)    # 판매가능여부
    available_order = models.BooleanField('주문가능여부', default=True)        # 주문가능여부

    created_at = models.DateTimeField('생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField('갱신 시간', auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.name

    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)
    """

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id])
