from apps.categories.models import Category
from commands.services import all_object, get_object


def get_all_products():
    return all_object(Category.objects,
                      select_related=('parent',),
                      prefetch_related=('children', 'children__children', 'children__children__children'),
                      )


def get_product(pk: int):
    """
    нужно сделать что бы select related b prefect related работал
    """
    category = get_object(Category.objects, pk=pk)
    return category
