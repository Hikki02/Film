from rest_framework import serializers
from .models import Category
from films.utils import RecursiveSerializser


class FilterCategorySerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveSerializser(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ('name', 'is_main', 'children')
