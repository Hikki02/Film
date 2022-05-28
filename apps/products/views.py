from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

from apps.products.models import Product, ProductUserRelation
from apps.products.serializers import ProductSerializer, ProductUserRelationSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.filter().prefetch_related('product_image', 'product_video',
                                                         'short_epis_desc')
    serializer_class = ProductSerializer


class ProductUserRelationCreate(ListCreateAPIView):
    serializer_class = ProductUserRelationSerializer
    queryset = ProductUserRelation.objects.all()