from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, delete_profile_picture

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/delete_picture/', delete_profile_picture, name='delete_profile_picture'),  # Neue URL
]
