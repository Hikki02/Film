from rest_framework import serializers as s

from apps.feedback.base import BaseSerializer
from apps.feedback.models import FeedBack
from apps.feedback import utils


class FeedbackSerializers(BaseSerializer):
    name = s.CharField(max_length=50)
    email = s.EmailField()
    type_message = s.ChoiceField(choices=utils.FEEDBACK_CHOICE)
    text = s.CharField()
    created_at = s.DateTimeField(read_only=True)

    def create(self, validated_data):
        return FeedBack.objects.create(**validated_data)

