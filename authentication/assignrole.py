from connectdb.connectMySQL import connect_mysql
from authentication.roles import ADMIN, LECTURER, STUDENT

VALID_ROLES = [ADMIN, LECTURER, STUDENT]


def assign_role(username, role):
    """
    Gán role cho user theo username
    """
    if role not in VALID_ROLES:
        print("Role không hợp lệ")
        return

    conn = connect_mysql()
    cursor = conn.cursor()

    # kiểm tra user tồn tại
    cursor.execute(
        "SELECT user_id FROM users WHERE username=%s",
        (username,)
    )
    user = cursor.fetchone()

    if not user:
        print(" Username không tồn tại")
        conn.close()
        return

    cursor.execute(
        "UPDATE users SET role=%s WHERE username=%s",
        (role, username)
    )
    conn.commit()
    conn.close()

    print(f"Đã gán role '{role}' cho user '{username}'")
