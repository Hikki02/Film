from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, password: str, **extra) -> None:
        self._validate(email=email, password=password)
        user = self.model(email=self.normalize_email(email),
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    email: str,
                    password: str) -> None:
        self._create(email, password)

    def create_superuser(self,
                         email: str,
                         password: str) -> None:
        self._create(email, password, is_staff=True, is_superuser=True, is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/uploads/%Y/%m/%d/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    class Meta:
        app_label = 'users'
        db_table = 'users'

    def __str__(self):
        return f'{self.username}'

    objects = UserManager()