from rest_framework import serializers

from apps.categories.serializers import CategorySerializer
from apps.products.models import ProductImage, ProductVideo, Product, Producer, ProductUserRelation


class BaseSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ...
        fields = ['created_at', 'updated_at']

    def create(self, validated_data: dict):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance: object, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


