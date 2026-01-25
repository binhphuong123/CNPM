from user_student.user import User


class Student(User):
    def __init__(self, user_id, username, password,
                 full_name, date_of_birth=None, gender=None, class_id=None):
        # Gọi constructor của lớp User (Liên kết với UserService)
        # Fix cứng role="Student" để phân quyền tự động
        super().__init__(user_id, username, password, role="Student")

        # Các thuộc tính định danh trong StudentService
        self.student_id = user_id  # Thường student_id trùng với user_id
        self.full_name = full_name

        # Các thông tin bổ sung
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.class_id = class_id  # Lưu ID thay vì object để dễ khớp với DB

        # Dữ liệu mở rộng
        self.grades = []
        self.notifications = []

    def __str__(self):
        return f"Student: {self.full_name} (ID: {self.student_id}) - Class: {self.class_id}"

    def to_dict(self):
        """Hỗ trợ chuyển đổi sang dict để hiển thị hoặc lưu trữ"""
        return {
            "student_id": self.student_id,
            "username": self.username,
            "full_name": self.full_name,
            "class_id": self.class_id,
            "role": self.role
        }
