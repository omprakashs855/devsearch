from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('account/', views.userAccount, name = 'account'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
]