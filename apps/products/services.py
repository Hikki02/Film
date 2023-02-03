from apps.products.models import Product
from commands.services import all_object, get_object


def get_all_product():
    return all_object(
        Product.objects
    )


def get_product_by_id(product_id):
    return get_object(
        Product.objects,
        pk=product_id
    )
