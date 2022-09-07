from rest_framework import generics

from .models import FeedBack
from .serializers import FeedbackSerializers


class CreateFeedback(generics.CreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedbackSerializers
