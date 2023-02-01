from django.db.models import Manager
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from commands.services import all_object, get_object


def get_all_products():
    return all_object(Category.objects,
                      select_related=('parent',),
                      prefetch_related=('children', 'children__children', 'children__children__children'),
                      )


def generateError(errorCode):
    return {
        'status': status.HTTP_404_NOT_FOUND,
        'data': {
            'error': True,
            'code': errorCode
        }
    }

def get_product(pk: int):
    """
    нужно сделать что бы select related b prefect related работал
    """
    try:
        category = get_object(Category.objects, pk=pk)
        return category
    except Category.DoesNotExist:
        return Response(**generateError('DOES_NOT_EXIST'))
