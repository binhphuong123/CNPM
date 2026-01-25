from authentication.login_logout import login
from authentication.session import get_current_user


def test_login():
    if login():
        user = get_current_user()
        print("Login thành công. Role:", user["role"])

    else:
        print("Login thất bại")


test_login()
