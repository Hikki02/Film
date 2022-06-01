from django.urls import path
from .views import ProductCommentCreateList

urlpatterns = [
    path('comment/', ProductCommentCreateList.as_view()),
]
