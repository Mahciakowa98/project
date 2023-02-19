from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile-management', views.profile_management, name='profile-management'),
    path('register-success', views.register_success, name='register-success'),
    path('manage-shipping', views.manage_shipping, name='manage-shipping'),
    path('track-orders', views.track_orders, name='track-orders'),
    
]