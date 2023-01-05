from rest_framework.serializers import ModelSerializer

from home.models import Product, Category, Brand

class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"






