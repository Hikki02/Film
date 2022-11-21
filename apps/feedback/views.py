from rest_framework import generics

from .models import FeedBack
from .serializers import FeedbackSerializer


class CreateFeedback(generics.CreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedbackSerializer
