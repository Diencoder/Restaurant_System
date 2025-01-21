from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Menu, Cart, CartItem
from .services.user_service import UserService
from app.services.table_service import get_all_tables, reserve_table_by_id
# Home
def get_home(request):
    return render(request, 'app/home.html')

# About
def about(request):
    return render(request, 'app/about.html')

# Services
def services_view(request):
    return render(request, 'app/services.html')

# Contact
def contact(request):
    return render(request, 'app/contact.html')

def team(request):
    return render(request, 'app/team.html')

def testimonial(request):
    return render(request, 'app/testimonial.html')

# Booking
def booking(request):
    return render(request, 'app/booking.html')

# Register
def view_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        result = UserService.register_user(email, username, password)
        if result['status'] == 'success':
            messages.success(request, result['message'])
            return redirect('login')
        else:
            messages.error(request, result['message'])

    return render(request, 'app/register.html')

# Login
def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserService.authenticate_user(username, password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'app/login.html')

# Logout
@login_required
def view_logout(request):
    logout(request)
    return redirect('login')

# Menu
def menu_view(request):
    menu_items = Menu.objects.all()
    paginator = Paginator(menu_items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/menu.html', {'page_obj': page_obj})

# Cart
@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'app/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

from django.shortcuts import render
from .models import Menu

def menu_view(request):
    # Lấy tất cả món ăn cho từng danh mục
    main_items = Menu.objects.filter(category='Main')
    drink_items = Menu.objects.filter(category='Drink')
    dessert_items = Menu.objects.filter(category='Dessert')

    # Phân trang với mỗi trang hiển thị 10 món
    main_paginator = Paginator(main_items, 10)
    drink_paginator = Paginator(drink_items, 10)
    dessert_paginator = Paginator(dessert_items, 10)

    # Lấy số trang hiện tại từ URL
    main_page_number = request.GET.get('main_page')
    drink_page_number = request.GET.get('drink_page')
    dessert_page_number = request.GET.get('dessert_page')

    # Lấy các trang hiện tại
    main_page_obj = main_paginator.get_page(main_page_number)
    drink_page_obj = drink_paginator.get_page(drink_page_number)
    dessert_page_obj = dessert_paginator.get_page(dessert_page_number)

    return render(request, 'app/menu.html', {
        'main_page_obj': main_page_obj,
        'drink_page_obj': drink_page_obj,
        'dessert_page_obj': dessert_page_obj,
    })


# Hiển thị danh sách bàn
def table_list(request):
    tables = get_all_tables()
    return render(request, 'app/table_list.html', {'tables': tables})

# Đặt bàn
def reserve_table(request, table_id):
    success, message = reserve_table_by_id(table_id)
    return HttpResponse(message)