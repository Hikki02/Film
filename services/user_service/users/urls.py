from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserCreateApiView, VerifyEmail

urlpatterns = [
    path('registration/', UserCreateApiView.as_view(), name='registration'),
    path('verify-email/<str:token>/', VerifyEmail.as_view(), name='verify-email'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
