from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('register/', views.view_register, name='register'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
    path('team/', views.team, name='team'),
    path('menu/', views.menu_view, name='menu'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('tables/', views.table_list, name='table_list'),
    path('reserve/<int:table_id>/', views.reserve_table, name='reserve_table'),
]
