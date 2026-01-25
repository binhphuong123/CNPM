from connectdb.connectMySQL import connect_mysql

from authentication.login_logout import login, logout
from authentication.session import get_current_user
from authentication.roles import ADMIN, LECTURER, STUDENT
from authentication.assignrole import assign_role

from security.change_reset_pass import change_password, reset_password

from lecturer_class.class_lecturer_service import LecturerClassService
from user_student.student_service import StudentService
from grade.Grade_service import GradeService
from notification.notification_service import NotificationService


# ================= INIT =================
conn = connect_mysql()

lecturer_class_service = LecturerClassService(conn)
student_service = StudentService(conn)
grade_service = GradeService(conn)
notification_service = NotificationService(conn)


# ================= ADMIN MENU =================
def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("---- User & Student Management ----")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")

        print("---- Lecturer & Class Management ----")
        print("4. Add lecturer")
        print("5. Update lecturer")
        print("6. Delete lecturer")
        print("7. Create class")
        print("8. Update class")
        print("9. Delete class")
        print("10. Assign lecturer to class")

        print("---- Security ----")
        print("11. Reset user password")
        print("12. Change my password")

        print("---- Notification ----")
        print("13. Send notification")

        print("14. Assign role to user")
        print("0. Logout")

        choice = input("Choose: ").strip()
        user = get_current_user()

        if choice == "1":
            student_id = input("Student ID: ")
            name = input("Full name: ")
            class_id = input("Class ID: ")
            student_service.add_student(user, student_id, name, class_id)

        elif choice == "2":
            student_id = input("Student ID: ")
            name = input("New name: ")
            class_id = input("New class ID: ")
            student_service.update_student(user, student_id, name, class_id)

        elif choice == "3":
            student_id = input("Student ID: ")
            student_service.delete_student(user, student_id)

        elif choice == "4":
            lecturer_id = input("Lecturer ID: ")
            name = input("Full name: ")
            lecturer_class_service.add_lecturer(user, lecturer_id, name)

        elif choice == "5":
            lecturer_id = input("Lecturer ID: ")
            name = input("New name: ")
            lecturer_class_service.update_lecturer(user, lecturer_id, name)

        elif choice == "6":
            lecturer_id = input("Lecturer ID: ")
            lecturer_class_service.delete_lecturer(user, lecturer_id)

        elif choice == "7":
            class_id = input("Class ID: ")
            class_name = input("Class name: ")
            lecturer_class_service.create_class(user, class_id, class_name)

        elif choice == "8":
            class_id = input("Class ID: ")
            class_name = input("New class name: ")
            lecturer_class_service.update_class(user, class_id, class_name)

        elif choice == "9":
            class_id = input("Class ID: ")
            lecturer_class_service.delete_class(user, class_id)

        elif choice == "10":
            lecturer_id = input("Lecturer ID: ")
            class_id = input("Class ID: ")
            lecturer_class_service.assign_lecturer_to_class(user, lecturer_id, class_id)

        elif choice == "11":
            username = input("Username: ")
            reset_password(username)

        elif choice == "12":
            change_password()

        elif choice == "13":
            student_id = input("Student ID: ")
            title = input("Title: ")
            content = input("Content: ")
            notification_service.send_notification(user, student_id, title, content)

        elif choice == "14":
            username = input("Username: ")

            print("Choose role:")
            print(f"1. {ADMIN}")
            print(f"2. {LECTURER}")
            print(f"3. {STUDENT}")

            r = input("Choose: ")

            if r == "1":
                role = ADMIN
            elif r == "2":
                role = LECTURER
            elif r == "3":
                role = STUDENT
            else:
                print("Invalid role")
                continue

            assign_role(username, role)

        elif choice == "0":
            logout()
            break

        else:
            print("Invalid choice")


# ================= LECTURER MENU =================
def lecturer_menu():
    while True:
        print("\n===== LECTURER MENU =====")
        print("1. Enter grade")
        print("2. Send notification")
        print("3. Change password")
        print("0. Logout")

        choice = input("Choose: ").strip()
        user = get_current_user()

        if choice == "1":
            student_id = input("Student ID: ")
            class_id = input("Class ID: ")
            score = input("Score: ")
            grade_service.enter_grade(user, student_id, class_id, score)

        elif choice == "2":
            student_id = input("Student ID: ")
            title = input("Title: ")
            content = input("Content: ")
            notification_service.send_notification(user, student_id, title, content)

        elif choice == "3":
            change_password()

        elif choice == "0":
            logout()
            break

        else:
            print("Invalid choice")


# ================= STUDENT MENU =================
def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. View my grades")
        print("2. View notifications")
        print("3. Change password")
        print("0. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            student_id = input("Your Student ID: ")
            grade_service.view_grades_by_student(student_id)

        elif choice == "2":
            student_id = input("Your Student ID: ")
            notifications = notification_service.view_notifications(student_id)

            if not notifications:
                print("No notifications")
            else:
                for n in notifications:
                    print(f"[{n['created_at']}] {n['title']}")
                    print(n["content"])
                    print("-" * 30)

        elif choice == "3":
            change_password()

        elif choice == "0":
            logout()
            break

        else:
            print("Invalid choice")


# ================= MAIN =================
def main():
    if not login():
        return

    user = get_current_user()
    role = user["role"]

    if role == ADMIN:
        admin_menu()
    elif role == LECTURER:
        lecturer_menu()
    elif role == STUDENT:
        student_menu()
    else:
        print("Unknown role")


if __name__ == "__main__":
    main()
