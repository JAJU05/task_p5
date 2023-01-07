from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ProductModelViewSet, CategoryModelViewSet, ShopRetrieveAPIView, ShopListCreateAPIView, \
    ProductImageModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('product-image', ProductImageModelViewSet, 'product_image')
router.register('category', CategoryModelViewSet, 'category')


urlpatterns = [
    path('', include(router.urls)),
    path('shop/',ShopListCreateAPIView.as_view()),
    path('shop/<str:uuid>/', ShopRetrieveAPIView.as_view()),
]





