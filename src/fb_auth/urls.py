from django.urls import path, include
from django.contrib.auth import views as auth_views
from fb_auth import views

app_name = "fb_auth"
urlpatterns = [
    path('login/', views.login, name = 'login'),

]