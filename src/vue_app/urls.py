from django.contrib import admin
from django.urls import path

from vue_app import views as vue_views


urlpatterns = [
    path('test/', vue_views.test_vue),
]
