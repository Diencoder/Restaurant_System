from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services_view, name='services'),
    path('menu/', views.menu_view, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    # Nếu logic `submit_booking` đã được chuyển sang service, xóa dòng này. 
    # Nếu cần giữ, đảm bảo chức năng `submit_booking` tồn tại trong views.py.
    # path('submit-booking/', views.submit_booking, name='submit_booking'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
    path('register/', views.views_register, name='register'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('tables/', views.table_list, name='table_list'),
    path('reserve/<int:table_id>/', views.reserve_table, name='reserve_table'),
]
