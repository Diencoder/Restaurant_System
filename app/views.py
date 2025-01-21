from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from app.services.auth_service import register_user, login_user, logout_user
from app.services.menu_service import get_menu_items_by_category
from app.services.cart_service import get_user_cart, get_cart_items, add_item_to_cart
from app.services.table_service import get_all_tables, reserve_table_by_id

# Trang chủ
def get_home(request):
    return render(request, 'app/home.html')

# Trang giới thiệu
def about(request):
    team = [
        {'name': 'Chef 1', 'position': 'Head Chef', 'image': 'app/img/team-1.jpg'},
        {'name': 'Chef 2', 'position': 'Sous Chef', 'image': 'app/img/team-2.jpg'},
        {'name': 'Chef 3', 'position': 'Pastry Chef', 'image': 'app/img/team-3.jpg'},
        {'name': 'Chef 4', 'position': 'Line Cook', 'image': 'app/img/team-4.jpg'},
    ]
    return render(request, 'app/about.html', {'team': team})

# Dịch vụ
def services_view(request):
    return render(request, 'app/services.html')

# Trang liên hệ
def contact(request):
    return render(request, 'app/contact.html')

# Trang đặt bàn
def booking(request):
    return render(request, 'app/booking.html')

# Đội ngũ nhân viên
def team(request):
    return render(request, 'app/team.html')

# Lời chứng thực
def testimonial(request):
    return render(request, 'app/testimonial.html')

# Đăng ký
def views_register(request):
    if request.method == 'POST':
        success, form = register_user(request)
        if success:
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

# Đăng nhập
def view_login(request):
    if request.method == 'POST':
        success, form = login_user(request)
        if success:
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

# Đăng xuất
@login_required
def view_logout(request):
    logout_user(request)
    return redirect('home')

# Hiển thị danh sách món ăn
def menu_view(request):
    main_items = get_menu_items_by_category('Main')
    drink_items = get_menu_items_by_category('Drink')
    dessert_items = get_menu_items_by_category('Dessert')

    return render(request, 'app/menu.html', {
        'main_items': main_items,
        'drink_items': drink_items,
        'dessert_items': dessert_items,
    })

# Hiển thị giỏ hàng
@login_required
def view_cart(request):
    cart = get_user_cart(request.user)
    cart_items = get_cart_items(cart)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'app/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Thêm món ăn vào giỏ hàng
@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
    add_item_to_cart(request.user, menu_item)
    return redirect('view_cart')

# Hiển thị danh sách bàn
def table_list(request):
    tables = get_all_tables()
    return render(request, 'app/table_list.html', {'tables': tables})

# Đặt bàn
def reserve_table(request, table_id):
    success, message = reserve_table_by_id(table_id)
    return HttpResponse(message)
