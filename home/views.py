from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from home.models import Product, Category
from home.serializers import ProductModelSerializer, CategoryModelSerializer

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("name", )


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
