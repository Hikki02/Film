
from django.urls import path
from .views import CreateFeedback

urlpatterns = [
    path('feedback/', CreateFeedback.as_view()),

]