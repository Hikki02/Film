from rest_framework import generics

from .serializers import CategorySerializer
from .models import Category
from .services import get_all_products, get_product


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return get_all_products()


class CategoryRetrieve(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_object(self, queryset=None):
        return get_product(pk=self.kwargs['pk'])
