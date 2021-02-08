from django.contrib import admin
from .models import Product, Category, MainCategory
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'weight', 'origin', 'packing_type', 'price', 'stock', 'delivery', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_category']


admin.site.register(MainCategory)