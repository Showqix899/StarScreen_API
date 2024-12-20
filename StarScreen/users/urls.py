
from django.urls import path

from .views import (
    NormalUserRegistrationView,
    AdminUserRegistrationView,
    LoginView,
    LogoutView,
    # VerifyEmailView
)

from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/normal/', NormalUserRegistrationView.as_view(), name='register_normal_user'),
    path('register/admin/', AdminUserRegistrationView.as_view(), name='register_admin_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
]


