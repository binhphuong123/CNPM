from authentication.login_logout import login, logout
from authentication.authorization import check_role
from authentication.roles import ADMIN, LECTURER, STUDENT

login()

role = check_role()

if role == ADMIN:
    print("User là admin")
elif role == LECTURER:
    print("User là lecturer")
elif role == STUDENT:
    print("User là student")
else:
    print("Chưa đăng nhập")

logout()
