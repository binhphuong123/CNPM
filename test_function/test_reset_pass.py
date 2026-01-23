from security.change_reset_pass import reset_password
from security.change_reset_pass  import change_password
from authentication.login_logout import login


def test_reset_password():

    username = "ad33min"
    default_password = "123456"

    # 1. Reset password
    reset_password(username)
    print(" Đã gọi reset_password()")

    # 2. Test login bằng mật khẩu mặc định
    login_success = login(username, default_password)

    if login_success:
        print("Reset password THÀNH CÔNG – login được bằng mật khẩu mặc định")
    else:
        print("Reset password THẤT BẠI – không login được")


if __name__ == "__main__":
    test_reset_password()
