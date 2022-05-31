from rest_framework import serializers
from .models import Category

class FilterCategorySerializer(serializers.ListSerializer):
    def to_representation(self,data):
        data= data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer= self.parent.parent.__class__(value,context=self.context)
        return serializer.data

class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterCategorySerializer
        model=Category
        fields=('name','is_main','children')