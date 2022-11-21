from rest_framework import serializers as s

from apps.feedback.models import FeedBack


class BaseSerializers(s.Serializer):
    id = s.UUIDField(read_only=True)

    class Meta:
        # you just need to create a Meta class and set the model
        # if you have the create method
        model = ...

    def create(self, validated_data: dict):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance: object, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FeedBackBaseSerializer(BaseSerializers):

    class Meta:
        model = FeedBack
