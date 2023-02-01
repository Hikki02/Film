import jwt
from decouple import config
from rest_framework import generics
from rest_framework import views, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import RegistrationSerializer
from apps.users.services import create_user, get_all_users, get_user_by_id, save_user


def validate(token) -> None:
    try:
        payload = jwt.decode(token, config('SECRET_KEY'),
                             algorithms=config('ALGORITHMS'))
        user = VerifyEmail.get_object(User, payload.get('user_id', None))
        if user.is_active:
            ...
        else:
            user.is_active = True
            save_user(user)
        return
    except jwt.ExpiredSignatureError:
        error = 'Activation Expired'
    except jwt.exceptions.DecodeError:
        error = 'Invalid token'
    raise ValidationError({'error': error},
                          status.HTTP_400_BAD_REQUEST)


class UserCreateApiView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        email = self.request.data.get('email')
        password = self.request.data.get('password')
        username = self.request.data.get('username')
        return create_user(email, password, username)

    def get_queryset(self):
        """need to optimize request"""
        return get_all_users()


class VerifyEmail(views.APIView):

    def get_object(self, id) -> object:
        user = get_user_by_id(id)
        return user

    def get(self, request, token):
        validate(token)
        return Response({'email': 'Successfully activated'},
                        status.HTTP_200_OK)
