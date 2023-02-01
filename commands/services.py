from django.db.models import Manager


def get_first_object_decorator(service_func: callable):
    def get_first_object_wrapper(objects, first_object=(), **kwargs):
        return service_func(objects, **kwargs).first(*first_object)

    return get_first_object_wrapper


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


@get_first_object_decorator
def filter_object(objects: Manager, **kwargs):
    return objects.filter(**kwargs)
