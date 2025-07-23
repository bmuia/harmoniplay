from django.urls import path
from .views import RegistrationView,LogoutView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register-user'),
    path('login/', MyTokenObtainPairView.as_view(), name='login-user'),
    path('login/refresh/',TokenRefreshView.as_view(), name='login-refresh-user'),
    path('logout/', LogoutView.as_view(), name='logout-user'),
]
