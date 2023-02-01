from rest_framework import generics, status
from rest_framework.response import Response

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
        category_id = self.kwargs['pk']
        category = get_product(category_id)
        # serializer = CategorySerializer(category)
        return category
