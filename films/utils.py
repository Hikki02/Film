from rest_framework import serializers as s


class RecursiveSerializser(s.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data
