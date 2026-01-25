import mysql.connector
from authentication.login_logout import login
from notification.notification_service import NotificationService


def show_menu():
    print("\n===== NOTIFICATION MANAGEMENT =====")
    print("1. Send notification ")
    print("2. View my notifications (STUDENT)")
    print("0. Exit")


def main():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_management_system",
        charset="utf8mb4"
    )

    service = NotificationService(conn)

    print("===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")
    current_user = login(username, password)

    if not current_user:
        print("Login failed")
        return

    print("Login success")

    while True:
        show_menu()
        choice = input("Choose: ")

        try:
            if choice == "1":
                service.send_notification(
                    current_user,
                    student_id=int(input("Student ID: ")),
                    title=input("Title: "),
                    content=input("Content: ")
                )


            elif choice == "2":

                student_id = int(input("Your student ID: "))

                notifications = service.view_notifications(student_id)

                if not notifications:

                    print("No notifications")

                else:

                    for n in notifications:
                        print(f"[{n['created_at']}] {n['title']}: {n['content']}")

            elif choice == "0":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)

    conn.close()


if __name__ == "__main__":
    main()
