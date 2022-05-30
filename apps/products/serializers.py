from rest_framework import serializers

from apps.products.models import (Product, ProductCategoryRelation, VideoProduct,
                                  ProductImage, ShortEpisodDesc, ProductUserRelation)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'image', 'is_main',
        )


class VideoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProduct
        fields = (
            'name', 'video',
        )


class ShortEpisodDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortEpisodDesc
        fields = (
            'name', 'desc',
        )


class ProductCategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryRelation
        fields = (
            'category', 'product',
        )


class ProductSerializer(serializers.ModelSerializer):
    category_product = ProductCategoryRelationSerializer(many=True, read_only=True)
    product_video = VideoProductSerializer(many=True, read_only=True)
    product_image = ProductImageSerializer(many=True, read_only=True)
    short_epis_desc = ShortEpisodDescSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'name', 'year_of_release', 'type',
            'num_of_ep', 'producer', 'desc', 'teg',
            'product_video', 'product_image', 'short_epis_desc',
            'category_product',
        )


class ProductUserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUserRelation
        fields = ('user', 'product', 'rate', 'is_bookmark')

    def create(self, validated_data):

        obj, _ = ProductUserRelation.objects.get_or_create(**validated_data, )
        return obj
