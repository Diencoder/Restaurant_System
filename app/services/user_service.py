from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserService:
    @staticmethod
    def register_user(email, username, password):
        if User.objects.filter(email=email).exists():
            return {'status': 'error', 'message': 'Email đã tồn tại'}
        if User.objects.filter(username=username).exists():
            return {'status': 'error', 'message': 'Username đã tồn tại'}

        User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        return {'status': 'success', 'message': 'Đăng ký thành công'}

    @staticmethod
    def authenticate_user(username, password):
        user = authenticate(username=username, password=password)
        return user
