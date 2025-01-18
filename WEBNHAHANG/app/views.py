from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.services.user_services import UserService

# Create your views here.
def get_home(request):
    return render(request,'app/home.html')

def about(request):
    team = [
        {'name': 'Chef 1', 'position': 'Head Chef', 'image': 'app/img/team-1.jpg'},
        {'name': 'Chef 2', 'position': 'Sous Chef', 'image': 'app/img/team-2.jpg'},
        {'name': 'Chef 3', 'position': 'Pastry Chef', 'image': 'app/img/team-3.jpg'},
        {'name': 'Chef 4', 'position': 'Line Cook', 'image': 'app/img/team-4.jpg'},
    ]
    return render(request, 'app/about.html', {'team': team})


def services_view(request):
    return render(request, 'app/services.html')  

def menu_view(request):
    return render(request, 'app/menu.html')

def contact(request):
    return render(request, 'app/contact.html')

def booking(request):
    return render(request, 'app/booking.html')

def submit_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        datetime = request.POST.get('datetime')
        people = request.POST.get('people')
        message = request.POST.get('message')
        # Xử lý dữ liệu booking tại đây
        return HttpResponse("Booking submitted successfully!")
    else:
        return HttpResponse("Invalid request method!")

def team(request):
    return render(request, 'app/team.html')

def testimonial(request):
    return render(request, 'app/testimonial.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Xác thực thông tin người dùng
        user = UserService.authenticate_user(username, password)

        if user:
            # Đăng nhập thành công
            request.session['user_id'] = user.id  # Lưu thông tin vào session
            return redirect('home')  # Chuyển hướng về trang chủ

        else:
            # Đăng nhập thất bại
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = UserService.register_user(email, username, password)

        # Kiểm tra kết quả từ service
        if 'error' in result:
            return render(request, 'register.html', {'error': result['error']})

        # Nếu thành công, chuyển hướng đến trang login
        return redirect('login')

    return render(request, 'register.html')