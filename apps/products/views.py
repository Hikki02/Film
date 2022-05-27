from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView

from apps.products.models import Product, ProductUserRelation
from apps.products.serializers import ProductSerializer, ProductUserRelationSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.filter().prefetch_related('product_image', 'product_video',
                                                         'short_epis_desc')
    serializer_class = ProductSerializer


class ProductUserRelationCreate(ListCreateAPIView):
    serializer_class = ProductUserRelationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)