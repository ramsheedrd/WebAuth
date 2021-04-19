
from django.urls import path
from .views import (
    register_view,
    login_view,
    home_view,
    logout_view,
    update_profile_view,
    update_password_view,
    upload_profile_image
)

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('home/', home_view),
    path('logout/', logout_view),
    path('update/', update_profile_view),
    path('password/', update_password_view),
    path('image/', upload_profile_image),
]
