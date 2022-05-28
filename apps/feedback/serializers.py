from rest_framework import serializers
from .models import FeedBack

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields=('name', 'email', 'type_message', 'text')
