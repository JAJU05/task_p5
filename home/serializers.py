from rest_framework.serializers import ModelSerializer

from home.models import Product, Category, Shop, ProductImage


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'description', 'image')


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product')
