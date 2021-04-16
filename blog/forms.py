from django import forms
from .models import BlogModel

class BlogAddForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content', 'image']