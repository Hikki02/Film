from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.CreateFeedback.as_view()),

]