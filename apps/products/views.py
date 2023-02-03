from rest_framework import generics

from apps.products.models import Product, ProductUserRelation
from apps.products.serializers import ProductSerializer
from apps.products.services import get_all_product, get_product_by_id


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return get_all_product()


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer

    def get_object(self):
        product_id = self.kwargs['pk']
        return get_product_by_id(product_id)
