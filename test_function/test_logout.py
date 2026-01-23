# test_logout.py
# =========================
# TEST LOGOUT FUNCTION
# =========================

from authentication.login_logout import login, logout
from authentication.session import get_current_user


def test_logout():
    print("=== TEST LOGOUT ===")

    # 1. Login trước
    is_login = login("admin", "admin123")
    if not is_login:
        print("Login thất bại → không thể test logout")
        return

    print(" Login thành công")

    # 2. Gọi logout
    logout()


    # 3. Kiểm tra session
    current_user = get_current_user()
    if current_user is None:
        print("Logout thành công")
    else:
        print("Logout thất bại")


if __name__ == "__main__":
    test_logout()
