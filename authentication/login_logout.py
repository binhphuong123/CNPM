from authentication.session import set_user,clear_user
from security.password_hash import hash_password
from connectdb.connectMySQL import connect_mysql

def login(username=None, password=None):
    """
    Đăng nhập hệ thống
    """


    if username is None:
        username = input("Username: ")
    if password is None:
        password = input("Password: ")

    conn = connect_mysql()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, hash_password(password))
    )

    user = cursor.fetchone()

    if user:
        set_user(user)
        print("Đăng nhập thành công")
        return True

    print(" Sai username hoặc password")
    return False

def logout():
    """
    Đăng xuất người dùng
    """
    clear_user()
    print("Đã đăng xuất")
