from django.urls import path
from .views import (
    product_create_view_raw_html,
    product_create_view_raw_django,
    render_initial_data,

    product_create_view,
    product_detail_view,
    product_update_view,
    product_list_view,
    product_delete_view,
)

app_name = 'products' # Namespacing!!!

urlpatterns = [
    path('create-raw-html/', product_create_view_raw_html),
    path('create-raw-django/', product_create_view_raw_django),
    path('initial/', render_initial_data),

    path('/', product_list_view, name='product-list'),
    path('create/', product_create_view, name = 'product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/update', product_update_view, name = 'product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),

]