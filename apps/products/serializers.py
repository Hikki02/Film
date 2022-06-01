from rest_framework import serializers

from apps.comments.serializers import ProductCommentSerializer
from apps.products.models import (Product, ProductVideo,
                                  ProductImage, ProductUserRelation)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'image', 'is_main',
        )


class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = (
            'name', 'video', 'desc'
        )


class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name', 'year_of_release', 'type',
            'num_of_ep', 'producer', 'desc', 'teg', 'product_image',
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    product_video = ProductVideoSerializer(many=True, read_only=True)
    product_image = ProductImageSerializer(many=True, read_only=True)
    product_comments = ProductCommentSerializer(many=True, )

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name', 'year_of_release', 'type',
            'num_of_ep', 'producer', 'desc', 'teg',
            'product_video', 'product_image',
            'product_comments'
        )

class ProductUserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUserRelation
        fields = ('user', 'product', 'rate', 'is_bookmark')

    def create(self, validated_data):
        obj, _ = ProductUserRelation.objects.get_or_create(**validated_data, )
        return obj
