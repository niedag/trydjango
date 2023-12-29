from django.urls import path, include
from .views import (
    test_view,
    JS_SDK_login_view
)

urlpatterns = [
    path('', test_view, name="test_view"),
    path('JSlogin', JS_SDK_login_view, name = "SDK_login")
]
