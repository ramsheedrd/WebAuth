from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BlogAddForm
from .models import BlogModel

# Create your views here.
@login_required
def create_blog_view(request):
    if request.method == "POST":
        form = BlogAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/')
        else:
            return render(request,'create_blog.html', {'form': form})
    else:
        form = BlogAddForm()
        return render(request,'create_blog.html', {'form': form})


@login_required
def delete_blog_view(request, id):
    blog = BlogModel.objects.get(id=id)
    if blog.user == request.user:
        blog.delete()
    return redirect('/')