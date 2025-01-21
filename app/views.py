from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Menu, Cart, CartItem  # Import model Menu
from django.core.paginator import Paginator
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

# Xử lý đặt bàn
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

# Đội ngũ nhân viên
def team(request):
    return render(request, 'app/team.html')

# Lời chứng thực
def testimonial(request):
    return render(request, 'app/testimonial.html')

# Đăng ký
def views_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

# Đăng nhập
def view_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

# Đăng xuất
@login_required
def view_logout(request):
    logout(request)
    return redirect('home')

# Hiển thị danh sách món ăn
# cách phân trang
# def menu_list(request):
#     # Lấy tất cả món ăn từ cơ sở dữ liệu
#     menu_items = Menu.objects.all()
    
#     # Phân trang, mỗi trang hiển thị 6 món ăn
#     paginator = Paginator(menu_items, 6)
#     page_number = request.GET.get('page')  # Lấy số trang từ request
#     page_obj = paginator.get_page(page_number)
    
#     # Truyền dữ liệu sang template
#     return render(request, 'app/test_menu.html', {'page_obj': page_obj})

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

@login_required
def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.all()
    total_price = sum(item.get_total_price() for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'app/cart.html', context)

@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)

    if not item_created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')

from django.shortcuts import render
from .models import Table

def table_list(request):
    # Lấy danh sách tất cả các bàn
    tables = Table.objects.all()
    return render(request, 'app/table_list.html', {'tables': tables})



from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Table

def reserve_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if table.reservation_status == 'Available':
        table.reservation_status = 'Reserved'
        table.save()
        return HttpResponse(f"Bàn {table.table_number} đã được đặt thành công!")
    else:
        return HttpResponse(f"Bàn {table.table_number} không khả dụng để đặt.")
