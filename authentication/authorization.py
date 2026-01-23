


from authentication.session import get_current_user
from authentication.roles import ADMIN, LECTURER, STUDENT


def check_role():
    """
    Trả về role của user hiện tại
    """
    user = get_current_user()

    if not user:
        return None

    return user.get("role")
