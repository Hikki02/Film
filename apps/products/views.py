from django.shortcuts import render
from django.db.models import Subquery, Prefetch
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView

from rest_framework.response import Response

from apps.comments.models import ProductComment
from apps.products.models import Product, ProductUserRelation
from apps.products.serializers import ProductSerializer, ProductUserRelationSerializer, ProductDetailSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.filter().prefetch_related('product_image')
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductDetailSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = Product.objects.filter(product_id=self.queryset)
    #     serializer = ProductDetailSerializer(instance=instance)
    #     return Response(serializer.data)


class ProductUserRelationCreateList(ListCreateAPIView):
    serializer_class = ProductUserRelationSerializer

    def get_queryset(self):
        return ProductUserRelation.objects.filter()
