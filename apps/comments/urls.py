from django.urls import path
from .views import ProductCommentCreate

urlpatterns = [
    path('comment/', ProductCommentCreate.as_view()),
]
