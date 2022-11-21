from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import CategorySerializer
from .models import Category


class CategoryList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter().select_related('parent'). \
        prefetch_related('children',
                         'children__children',
                         'children__children__children')
