from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from apps.newsletter.models import Newsletter


class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, username: str, password: str, **extra) -> None:
        self._validate(email=email, username=username, password=password)
        user = self.model(email=self.normalize_email(email),
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    email: str,
                    username: str,
                    password: str) -> None:
        self._create(email, password, username)

    def create_superuser(self,
                         email: str,
                         username: str,
                         password: str) -> None:
        self._create(email, username, password, is_staff=True, is_superuser=True, is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/uploads/%Y/%m/%d/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    newsletters = models.ManyToManyField(Newsletter, through='Subscription')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        app_label = 'users'
        db_table = 'users'

    def __str__(self):
        return f'{self.username}'

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    objects = UserManager()


class Subscription(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriber.username + ' Subscribed to ' + self.newsletter.name


