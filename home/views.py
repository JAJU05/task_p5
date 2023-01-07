import itertools
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from home.filters import ProductFilter
from home.models import Product, Category, Shop, ProductImage
from home.serializers import ProductModelSerializer, CategoryModelSerializer, ShopModelSerializer, \
    ProductImageModelSerializer


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
    filterset_class = ProductFilter


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ShopListCreateAPIView(ListCreateAPIView):
    queryset = Shop.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = ShopModelSerializer


class ShopRetrieveAPIView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageModelSerializer
