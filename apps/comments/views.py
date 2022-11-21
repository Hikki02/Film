from django.db.models import Prefetch
from rest_framework.generics import ListCreateAPIView

from apps.comments.models import ProductComment
from apps.comments.serializers import ProductCommentSerializer


class ProductCommentCreate(ListCreateAPIView):
    serializer_class = ProductCommentSerializer
    queryset = ProductComment.objects.filter(parent__isnull=True, is_active=True).\
        select_related('parent', 'user', 'product') \
        .prefetch_related(Prefetch('is_active__True'), 'children',
                          'children__children', 'children__children__children')
