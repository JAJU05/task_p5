from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from home.models import Product, Category, Shop
from home.serializers import ProductModelSerializer, CategoryModelSerializer, ShopModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['price']
    # filterset_fields = {
    #     'price': ['gte', 'lte'],
    #     'category': ['exact'],
    #     'shop': ['exact'],
    # }


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer



