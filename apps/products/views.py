from django.shortcuts import render
from django.db.models import Subquery
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

    def retrieve(self, request, *args, **kwargs):
        comments = ProductComment.objects.filter(is_active=True, product_id=self.queryset)

        return Response( status=status.HTTP_200_OK)


class ProductUserRelationCreateList(ListCreateAPIView):
    serializer_class = ProductUserRelationSerializer

    def get_queryset(self):
        return ProductUserRelation.objects.filter(user=self.request.user)
