from rest_framework.generics import CreateAPIView

from apps.comments.models import ProductComment
from apps.comments.serializers import ProductCommentSerializer


class ProductCommentCreate(CreateAPIView):
    serializer_class = ProductCommentSerializer
    queryset = ProductComment.objects.filter()
