"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from pages.views import homepage_view
from pages.views import about_view
from pages.views import hello_world_view


# Products
from products.views import (
    product_detail_view,
    product_create_view,
    product_create_view_raw_html,
    product_create_view_raw_django,
    render_initial_data,
    dynamic_lookup_view,
    product_list_view,
    product_delete_view,
)


# Facebook testing
from facetest.views import display_my_facebook_post
from facetest.views import facetest_view
from facetest.views import facemsg_view
#from facetest.views import json_display_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name ='home'),
    path('hello-world/', hello_world_view),
    path('about/', about_view),
    path('products/', product_detail_view),
    path('create/', product_create_view),
    path('create-raw-html/', product_create_view_raw_html),
    path('create-raw-django/', product_create_view_raw_django),
    path('initial/', render_initial_data),
    path('prod/<int:my_id>/', dynamic_lookup_view, name = 'product-detail'),
    path('prod/', product_list_view, name = 'product-list'),
    path('prod/<int:my_id>/delete/', product_delete_view, name = 'product-delete'),

    path('my-facebook-post/', display_my_facebook_post),
    path('facetest/', facetest_view),
    path('facemsg/', facemsg_view),
    #path('display_json/', json_display_view, name = 'json_display_page'),


]
