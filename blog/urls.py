from django.urls import path
from .views import BlogCreateView, create_blog_view, delete_blog_view

urlpatterns = [
    path('add/', BlogCreateView.as_view()),
    path('delete/<int:id>/', delete_blog_view)
]