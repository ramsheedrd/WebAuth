from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogModel(models.Model):
    id = models.BigAutoField(primary_key=True) 
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_image')

    