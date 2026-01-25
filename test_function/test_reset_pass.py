from security.change_reset_pass import reset_password

def main():
    print("===== TEST RESET PASSWORD =====")
    username = input("Nhập username cần reset mật khẩu: ")

    if not username:
        print(" Username không được để trống")
        return

    reset_password(username)
    print(" Reset mật khẩu xong ")

if __name__ == "__main__":
    main()
