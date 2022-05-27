
from django.urls import path

from .views import ProductList, ProductUserRelationCreate

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product-rate/', ProductUserRelationCreate.as_view()),

]
