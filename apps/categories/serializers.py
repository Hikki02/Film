from rest_framework import serializers as s
from .models import Category
from films.utils import RecursiveSerializser


class FilterCategorySerializer(s.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CategorySerializer(s.Serializer):
    name = s.CharField(max_length=225)
    children = RecursiveSerializser(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
