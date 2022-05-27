from django.shortcuts import render

from rest_framework.generics import ListAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.filter().prefetch_related('product_image', 'product_video',
                                                         'short_epis_desc')
    serializer_class = ProductSerializer
