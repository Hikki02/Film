from rest_framework import serializers

from .base import BaseSerializer
from .models import Product, ProductImage, ProductVideo


class ProductImageSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('product', 'image', 'is_main')


class ProductVideoSerializer(BaseSerializer, serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = ('product', 'name', 'video', 'description')


class ProductSerializer(serializers.ModelSerializer):
    liked_by = serializers.Serializer(source='user')
    product_video = ProductVideoSerializer(many=True)
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'year_of_release', 'type',
            'num_of_ep', 'description', 'teg', 'producer', 'liked_by', 'category',
            'is_ongoing',
            'product_video', 'product_image')