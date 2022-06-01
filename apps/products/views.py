from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView

from apps.comments.models import ProductComment
from apps.products.models import Product, ProductUserRelation
from apps.products.serializers import ProductSerializer, ProductUserRelationSerializer, ProductDetailSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.filter().prefetch_related('product_image')
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductDetailSerializer


class ProductUserRelationCreateList(ListCreateAPIView):
    serializer_class = ProductUserRelationSerializer

    def get_queryset(self):
        """лучше думаю сделать внутри на serialiser"""
        return ProductUserRelation.objects.filter(user=self.request.user)
