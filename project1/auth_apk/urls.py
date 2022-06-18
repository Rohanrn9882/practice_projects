from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerView, name="register_url"),
    path('login/', views.loginview, name="login_url"),
    path('logout/', views.logoutView, name="logout_url"),
    path('otp/', views.otpverificationView, name ="otp_url")
]