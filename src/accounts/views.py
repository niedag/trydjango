from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView): # From Django library - visit
    form_class = UserCreationForm
    success_url = reverse_lazy("templates:signup")
    template_name = "registration/signup.html"
