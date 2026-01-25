from connectdb.connectMySQL import connect_mysql
from authentication.session import get_current_user
from security.password_hash import hash_password


def change_password():
    """
    Đổi mật khẩu cho user đang đăng nhập
    """
    user = get_current_user()
    if not user:
        print("Chưa đăng nhập")
        return

    old_pass = input("Mật khẩu cũ: ")
    new_pass = input("Mật khẩu mới: ")

    conn = connect_mysql()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT password FROM users WHERE user_id=%s",
        (user["user_id"],)
    )
    db_pass = cursor.fetchone()["password"]

    if hash_password(old_pass) != db_pass:
        print(" Mật khẩu cũ không đúng")
        return

    cursor.execute(
        "UPDATE users SET password=%s WHERE user_id=%s",
        (hash_password(new_pass), user["user_id"])
    )
    conn.commit()

    print(" Đổi mật khẩu thành công")


def reset_password(username):
    """
    Reset mật khẩu về mặc định (ADMIN)
    """
    new_pass = "123456"

    conn = connect_mysql()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET password=%s WHERE username=%s",
        (hash_password(new_pass), username)
    )
    conn.commit()

    print("Mật khẩu đã reset.")
