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
    video = ProductVideoSerializer(many=True, source='product_video')
    images = ProductImageSerializer(many=True, source='product_image')
    comments = ProductCommentSerializer(many=True, source='product_comments')

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name', 'year_of_release', 'type',
            'num_of_ep', 'producer', 'desc', 'teg',
            'video', 'images',
            'comments'
        )




class ProductUserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUserRelation
        fields = ('user', 'product', 'rate', 'is_bookmark')

    def create(self, validated_data):
        obj, _ = ProductUserRelation.objects.get_or_create(**validated_data, )
        return obj
