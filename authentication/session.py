#Lưu trạng thái người dùng đang đăng nhập
_current_user = None


def set_user(user):

#Lưu thông tin user sau khi đăng nhập
    global _current_user
    _current_user = user


def get_current_user():

    #Lấy user hiện tại trong session

    return _current_user


def clear_user():

    #Xoá session khi logout

    global _current_user
    _current_user = None
