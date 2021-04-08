
from django.urls import path
from .views import register_view, login_view, home_view, logout_view

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('home/', home_view),
    path('logout/', logout_view),



]
