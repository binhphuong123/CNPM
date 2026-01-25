from authentication.login_logout import login, logout
from authentication.session import get_current_user

def main():
    print("===== TEST LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    user = login(username, password)

    if not user:
        print("Login thất bại, không test logout được")
        return

    print("\nĐang đăng nhập với user:")
    print(user)

    print("\n===== TEST LOGOUT =====")
    logout()

    print("\nKiểm tra user sau logout:")
    print(get_current_user())   # phải là None

    if get_current_user() is None:
        print("Logout hoạt động đúng")
    else:
        print("Logout bị lỗi")

if __name__ == "__main__":
    main()
