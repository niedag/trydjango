from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (
    SignUpView,
)

app_name = "accounts"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name = "password-reset"),
]