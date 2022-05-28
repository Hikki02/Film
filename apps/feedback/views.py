from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import FeedbackSerializers


class CreateFeedback(APIView):
    def post(self, request):
        print(request.data)
        serializer=FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)





