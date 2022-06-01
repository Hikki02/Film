from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import CategorySerializer
from .models import Category


class CategoryList(ListAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
