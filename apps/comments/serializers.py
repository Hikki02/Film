from rest_framework import serializers as s

from apps.categories.serializers import RecursiveSerializer
from apps.comments.models import ProductComment


class RecursiveField(s.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data


class ProductCommentSerializer(s.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = ProductComment
        fields = ('parent', 'user', 'product', 'text', 'created_at', 'children',)
