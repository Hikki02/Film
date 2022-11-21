from rest_framework import serializers

from apps.categories.serializers import CategorySerializer
from apps.products.models import ProductImage, ProductVideo, Product, Producer, ProductUserRelation


class BaseSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        # you just need to create a Meta class and set the model
        # if you have the create method
        model = ...
        fields = ['created_at', 'updated_at']

    def create(self, validated_data: dict):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance: object, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class BaseSocialSerializer(BaseSerializer, serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = ...
        fields = BaseSerializer.Meta.fields + ['title', 'user', ]


class BaseProductImageSerializer(BaseSerializer, serializers.ModelSerializer):
    image = serializers.ImageField()
    is_main = serializers.BooleanField(default=False)

    class Meta:
        model = ProductImage
        fields = BaseSerializer.Meta.fields + ['image', 'is_main']


class BaseProductVideoSerializer(BaseSerializer, serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    video = serializers.FileField()
    desc = serializers.CharField()

    class Meta:
        model = ProductVideo
        fields = BaseSerializer.Meta.fields + ['name', 'video', 'desc']


class BaseProducerSerializer(BaseSerializer, serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Producer
        fields = BaseSerializer.Meta.fields + ['name']


class BaseProductSerializer(BaseSerializer, serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    year_of_release = serializers.IntegerField()
    type = serializers.CharField(max_length=50)
    num_of_ep = serializers.CharField(max_length=125)
    desc = serializers.CharField()
    teg = serializers.CharField(max_length=225)

    product_image = BaseProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = BaseSerializer.Meta.fields + ['name', 'year_of_release', 'type', 'num_of_ep', 'producer',
                                               'description', 'teg', 'product_image', 'category', ]


class BaseProductUserRelationSerializer(BaseSerializer, serializers.ModelSerializer):

    class Meta:
        model = ProductUserRelation
        fields = BaseSerializer.Meta.fields + ['user', 'product', 'is_bookmark', 'rate']
