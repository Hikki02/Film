
from django.urls import path

from .views import ProductList, ProductUserRelationCreateList, ProductDetail

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),

    path('product-rate/', ProductUserRelationCreateList.as_view()),

]
