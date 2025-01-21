from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_user(request):
    """Xử lý đăng ký người dùng"""
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return True, form
    return False, form

def login_user(request):
    """Xử lý đăng nhập người dùng"""
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return True, form
    return False, form

def logout_user(request):
    """Xử lý đăng xuất người dùng"""
    logout(request)
