from django.contrib import admin
from django.urls import path
from app import views 
urlpatterns = [
    path('', views.get_home, name = 'home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('services/', views.services_view, name='services'),  
    path('menu/', views.menu_view, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),        
    path('submit-booking/', views.submit_booking, name='submit_booking'), 
    path('team/', views.team, name='team'),                 
    path('testimonial/', views.testimonial, name='testimonial'),
]