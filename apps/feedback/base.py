from rest_framework import serializers as s


class BaseSerializer(s.Serializer):
    id = s.IntegerField(read_only=True)

    def create(self, validated_data):
        super().create(validated_data)
        return validated_data

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        return validated_data

