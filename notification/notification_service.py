from authentication.authorization import check_role, ADMIN
from connectdb.connectMySQL import connect_mysql


class NotificationService:
    """
    Notification Management
    Actor: Administrator
    """

    def __init__(self, conn):
        self.conn = conn

    def send_notification(self, sender, student_id, title, content):
        check_role()

        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO notifications (student_id, title, content)
            VALUES (%s, %s, %s)
            """,
            (student_id, title, content)
        )
        self.conn.commit()
        print("Notification sent")

    def view_notifications(self, student_id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT notification_id, title, content, created_at
            FROM notifications
            WHERE student_id = %s
            ORDER BY created_at DESC
            """,
            (student_id,)
        )
        return cursor.fetchall()
