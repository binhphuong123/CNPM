from authentication.login_logout import login
from security.change_reset_pass import change_password


def test_change_password():
    print("=== TEST CHANGE PASSWORD ===")

    user = login()              # ✅ LẤY USER
    if not user:
        print(" Login thất bại, không test được")
        return

    change_password()           # ✅ HÀM TỰ LẤY USER TỪ SESSION


if __name__ == "__main__":
    test_change_password()
