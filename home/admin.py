from django.contrib import admin

from .models import Product, Category, Shop, ProductImage

admin.site.register((Shop, Category, Product, ProductImage))
