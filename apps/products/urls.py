
from django.urls import path

from .views import ProductList, ProductUserRelationCreateList

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product-rate/', ProductUserRelationCreateList.as_view()),

]
