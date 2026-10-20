from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('profile/', create_profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-food/', add_food, name='add_food'),
]
