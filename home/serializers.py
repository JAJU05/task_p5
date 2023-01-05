from uuid import uuid4

from rest_framework.serializers import ModelSerializer

from home.models import Category, Shop, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'description', 'image')


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')




