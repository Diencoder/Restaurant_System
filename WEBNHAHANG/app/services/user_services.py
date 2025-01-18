from django.contrib.auth.hashers import make_password, check_password
from app.models import User
class UserService:
    @staticmethod
    def register_user(email, username, password):
        # Kiểm tra email đã tồn tại
        if User.objects.filter(email=email).exists():
            return {'error': 'Email Đã Tồn Tại'}

        # Kiểm tra username đã tồn tại
        if User.objects.filter(username=username).exists():
            return {'error': 'Username Đã Tồn Tại'}

        # Lưu thông tin người dùng
        hashed_password = make_password(password)
        User.objects.create(
            email=email,
            username=username,
            password=hashed_password,
        )

        return {'success': 'User registered successfully!'}
    @staticmethod
    def authenticate_user(username, password):
        """
        Xác thực người dùng dựa trên username và password.
        """
        try:
            user = User.objects.get(username=username)
            # Kiểm tra mật khẩu
            if check_password(password, user.password):
                return user  # Nếu đúng trả về đối tượng người dùng
            else:
                return None  # Sai mật khẩu
        except User.DoesNotExist:
            return None  # Người dùng không tồn tại