from apps.users.models import User
from apps.users.utils import save_user_and_checking_for_uniqueness, _send_email
from commands.services import all_object, filter_object


def create_user(email: str, password: str, username: str) -> User:
    user = User(email=email, username=username, password=password)
    user.set_password(password)
    save_user_and_checking_for_uniqueness(user)
    _send_email(user)
    return user


def get_all_users():
    return all_object(
        User.objects
    )


def get_user_by_id(user_id):
    try:
        user = filter_object(User.objects, id=user_id, first_object=())
        return user
    except User.DoesNotExist:
        return None
