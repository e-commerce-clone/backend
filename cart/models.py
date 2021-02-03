from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from shop.models import Product
from photo.models import Product_photo
from accounts.models import Profile


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    photo = models.ForeignKey(Product_photo, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(null=True,default=1,validators=[MinValueValidator(1),
                                                                           MaxValueValidator(100)])

    class Meta:
        db_table= 'CartItem'

    def sub_total(self):
        return self.photo.product.price * self.quantity

    def __str__(self):
        return self.photo.product.name
