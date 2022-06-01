from .models import Category
from rest_framework import serializers as s


class RecursiveSerializer(s.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(s.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = 'id', 'name', 'is_main', 'children'
