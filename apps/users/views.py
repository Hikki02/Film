import jwt
from decouple import config
from rest_framework import views, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import RegistrationSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = RegistrationSerializer


class VerifyEmail(views.APIView):

    def get_object(self, model: User, id) -> object:
        obj = model.objects.filter(id=id).first()
        return obj

    def save_obj(self, obj: User) -> None:
        obj.save()

    def validate(self, token) -> None:
        try:
            payload = jwt.decode(token, config('SECRET_KEY'),
                                 algorithms=config('ALGORITHMS'))
            user = self.get_object(User, payload.get('user_id', None))
            if user.is_active:
                ...
            else:
                user.is_active = True
                self.save_obj(user)
            return
        except jwt.ExpiredSignatureError:
            error = 'Activation Expired'
        except jwt.exceptions.DecodeError:
            error = 'Invalid token'
        raise ValidationError({'error': error},
                              status.HTTP_400_BAD_REQUEST)

    def get(self, request, token):
        self.validate(token)
        return Response({'email': 'Successfully activated'},
                        status.HTTP_200_OK)
