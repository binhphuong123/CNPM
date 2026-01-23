from authentication.login_logout import login
from security.change_reset_pass import change_password


def test_change_password():


    if not login():
        print(" Login thất bại, không test được")
        return

    change_password()


if __name__ == "__main__":
    test_change_password()
