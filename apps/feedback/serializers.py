from rest_framework import serializers as s

from apps.feedback.base import BaseSerializers, FeedBackBaseSerializer

from apps.feedback import utils


class FeedbackSerializer(FeedBackBaseSerializer):
    name = s.CharField(max_length=50)
    email = s.EmailField()
    type_message = s.ChoiceField(choices=utils.FEEDBACK_CHOICE)
    text = s.CharField()
    created_at = s.DateTimeField(read_only=True)


