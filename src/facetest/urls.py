from django.urls import path

from .views import (
    display_my_facebook_post,
    facetest_view,
    facemsg_view
)

urlpatterns = [
    path('my-facebook-post/', display_my_facebook_post),
    path('facetest/', facetest_view),
    path('facemsg/', facemsg_view),
]