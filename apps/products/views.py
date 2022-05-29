from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView

from apps.products.models import Product, ProductUserRelation
from apps.products.serializers import ProductSerializer, ProductUserRelationSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.filter().prefetch_related('product_image', 'product_video',
                                                         'short_epis_desc')
    serializer_class = ProductSerializer


class ProductUserRelationCreateList(ListCreateAPIView):
    serializer_class = ProductUserRelationSerializer

    def get_queryset(self):
        """лучше думаю сделать внутри на serialiser"""
        return ProductUserRelation.objects.filter(user=self.request.user)
