from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from apps.comments.models import ProductComment
from apps.comments.serializers import ProductCommentSerializer


class ProductCommentCreateList(ListCreateAPIView):
    serializer_class = ProductCommentSerializer
    queryset = ProductComment.objects.all()
