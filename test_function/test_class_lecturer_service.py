from connectdb.connectMySQL import connect_mysql
from authentication.login_logout import login
from authentication.authorization import ADMIN
from lecturer_class.class_lecturer_service import LecturerClassService


def show_menu():
    print("\n===== LECTURER & CLASS MANAGEMENT =====")
    print("1. Add lecturer")
    print("2. Update lecturer")
    print("3. Delete lecturer")
    print("4. Create class")
    print("5. Update class")
    print("6. Delete class")
    print("7. Assign lecturer to class")
    print("0. Exit")


def main():
    conn = connect_mysql()
    service = LecturerClassService(conn)

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
                lecturer_id = int(input("Lecturer ID: "))
                full_name = input("Full name: ")
                service.add_lecturer(current_user, lecturer_id, full_name)

            elif choice == "2":
                lecturer_id = int(input("Lecturer ID: "))
                new_name = input("New name: ")
                service.update_lecturer(current_user, lecturer_id, new_name)

            elif choice == "3":
                lecturer_id = int(input("Lecturer ID: "))
                service.delete_lecturer(current_user, lecturer_id)

            elif choice == "4":
                class_id = int(input("Class ID: "))
                class_name = input("Class name: ")
                service.create_class(current_user, class_id, class_name)

            elif choice == "5":
                class_id = int(input("Class ID: "))
                new_name = input("New class name: ")
                service.update_class(current_user, class_id, new_name)

            elif choice == "6":
                class_id = int(input("Class ID: "))
                service.delete_class(current_user, class_id)

            elif choice == "7":
                lecturer_id = int(input("Lecturer ID: "))
                class_id = int(input("Class ID: "))
                service.assign_lecturer_to_class(current_user, lecturer_id, class_id)

            elif choice == "0":
                print("Exit")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)

    conn.close()


if __name__ == "__main__":
    main()
