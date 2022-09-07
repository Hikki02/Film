from rest_framework import serializers as s
from films.utils import RecursiveSerializser, FilterCategorySerializer
from apps.comments.models import ProductComment


class ChildrenSerializer(s.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ('user', 'product', 'text', 'created_at', 'is_active',)


class ProductCommentSerializer(s.ModelSerializer):
    children = RecursiveSerializser(many=True)

    class Meta:
        model = ProductComment
        fields = ('user', 'product', 'text', 'created_at', 'is_active', 'is_active', 'children',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        # children = instance.children.filter(is_active=True)
        response['children'] = ChildrenSerializer(instance.children, many=True).data
        return response

