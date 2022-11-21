from rest_framework import serializers
from apps.products.models import (ProductUserRelation, Product)
from .base import BaseProductSerializer, BaseProductVideoSerializer, BaseProductUserRelationSerializer, BaseSerializer
from .settings import RATE_CHOICE
from .. import users
from ..users.serializers import UserProfileSerializer

from apps.users.models import User


class ProductSerializer(BaseProductSerializer):
    ...


class ProductDetailSerializer(BaseProductSerializer):
    product_video = BaseProductVideoSerializer(many=True)

    class Meta:
        model = Product
        fields = BaseProductSerializer.Meta.fields + ['product_video']
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     comments = instance.comments.filter(is_active=True)
    #     response['comments'] = ProductCommentSerializer(instance.comments, many=True).data
    #     return response


# class ProductUserRelationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductUserRelation
#         fields = ('user', 'product'
#         , 'rate', 'is_bookmark')
#
#     def create(self, validated_data):
#         obj, _ = ProductUserRelation.objects.get_or_create(**validated_data, )
#         return obj

class UserSerializer(BaseSerializer):
    username = serializers.CharField(max_length=225)

    class Meta:
        model = User


class ProductUserRelationSerializer(BaseProductUserRelationSerializer):
    ...
