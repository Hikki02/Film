from django.db import IntegrityError
from rest_framework import serializers as s
from rest_framework.exceptions import ValidationError

from .models import User
from .settings import Email


class RegistrationSerializer(s.ModelSerializer):
    password = s.CharField(max_length=128, min_length=8, write_only=True)
    password2 = s.CharField(write_only=True)
    email = s.EmailField(required=True)

    class Meta:
        model = User
        fields = 'id', 'email', 'username', 'password', 'password2',

    def validate(self, attrs) -> dict[str, str]:
        password, password2 = attrs.get('password', None), \
                              attrs.pop('password2', None)
        if password != password2:
            raise s.ValidationError({'error': "Пароли не совподают"})
        return attrs

    def save_and_checking_for_uniqueness(self, user: User) -> None:
        try:
            user.save()
        except IntegrityError:
            raise ValidationError({
                'error': 'Уже такой юзер существует'
            })

    def _send_email(self, user: User) -> None:
        email = Email(user)
        email.send()

    def create(self, validated_data) -> dict:
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        self.save_and_checking_for_uniqueness(user)
        self._send_email(user)
        return validated_data


class UserProfileSerializer(s.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
