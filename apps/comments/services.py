from apps.comments.models import ProductComment
from commands.services import get_object, all_object


def get_all_comments():
    return all_object(
        ProductComment.objects
    )


