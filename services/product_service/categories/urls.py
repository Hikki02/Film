from django.urls import path


from . import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryRetrieve.as_view()),

]