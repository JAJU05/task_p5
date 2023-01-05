from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ProductModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('category', CategoryModelViewSet, 'category')


urlpatterns = [
    path('', include(router.urls)),
]






