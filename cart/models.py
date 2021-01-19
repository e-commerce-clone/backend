"""
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from shop.models import Product
from accounts.models import Profile

class CartItem(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    quantity=models.PositiveIntegerField(null=True,default=1,validators=[MinValueValidator(1),
                                                                         MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table= 'CartItem'

    def sub_total(self):
        return self.product.price*self.quantity

    def __str__(self):
        return self.product.name"""