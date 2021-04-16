from django.urls import path
from .views import create_blog_view, delete_blog_view

urlpatterns = [
    path('add/', create_blog_view),
    path('delete/<int:id>/', delete_blog_view)
]