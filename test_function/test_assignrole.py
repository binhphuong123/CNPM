from authentication.assignrole import assign_role
from authentication.roles import ADMIN, LECTURER, STUDENT


def main():
    print("===== TEST ASSIGN ROLE =====")
    print(f"Role hợp lệ: {ADMIN}, {LECTURER}, {STUDENT}")

    username = input("Nhập username: ").strip()
    role = input("Nhập role: ").strip().upper()

    if not username or not role:
        print(" Không được để trống")
        return

    assign_role(username, role)


if __name__ == "__main__":
    main()
