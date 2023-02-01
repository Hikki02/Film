from rest_framework import serializers as s

from .models import User


class RegistrationSerializer(s.ModelSerializer):
    password = s.CharField(max_length=128, min_length=8, write_only=True)
    password2 = s.CharField(write_only=True)
    email = s.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password2',)

    def validate(self, attrs) -> dict[str, str]:
        password, password2 = attrs.get('password', None), \
                              attrs.pop('password2', None)
        if password != password2:
            raise s.ValidationError({'error': "Пароли не совподают"})
        return attrs


class UserProfileSerializer(s.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
