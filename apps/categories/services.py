from django.db.models import Manager

from apps.categories.models import Category


def select_related_decorator(service_func: callable):
    def select_related_wrapper(objects, select_related=(), **kwargs):
        return service_func(objects, **kwargs).select_related(*select_related)

    return select_related_wrapper


def prefetch_related_decorator(service_func: callable):
    def prefetch_related_wrapper(objects, prefetch_related=(), **kwargs):
        return service_func(objects, **kwargs).prefetch_related(*prefetch_related)
    return prefetch_related_wrapper


def only_field_decorator(service_func: callable):
    def only_field_wrapper(objects, only=(), **kwargs):
        return service_func(objects, **kwargs).only(*only)

    return only_field_wrapper


@select_related_decorator
@prefetch_related_decorator
@only_field_decorator
def all_object(objects: Manager, **kwargs):
    return objects.all(**kwargs)


# @select_related_decorator
def get_object(objects: Manager, **kwargs):
    return objects.get(**kwargs)


def get_all_products():
    return all_object(Category.objects,
                      select_related=('parent',),
                      prefetch_related=('children', 'children__children', 'children__children__children'),
                      )


def get_product(pk: int):
    """
    нужно сделать что бы select related b prefect related работал
    """
    return get_object(
        Category.objects,
        # select_related=('parent',),
        pk=pk,
    )
