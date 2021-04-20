from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UpdationForm, ProfileImageForm

from blog.models import BlogModel
from django.views.generic import FormView, TemplateView, ListView, DetailView
# Create your views here.

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/accounts/login'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/accounts/home/')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/accounts/home/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password=password)
        if user:
            
            login(request, user)
            return redirect('/accounts/home')
        else:
            return redirect('/accounts/login')
    else:
        return render(request, 'login.html')



@login_required
def home_view(request):
    blogs = BlogModel.objects.all()
    return render(request, 'home.html', {'blogs':blogs})


class HomeView(ListView):
    template_name = 'home.html'
    model = BlogModel
    context_object_name = 'blogs'
    paginate_by = 10

class BlogView(DetailView):
    template_name = 'home.html'
    model = BlogModel
    context_object_name = 'blog'


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

@login_required
def upload_profile_image(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/accounts/home')
        else:
            return render(request, 'upload_profile_image.html', {'form': form})

    else:
        form = ProfileImageForm()
        return render(request, 'upload_profile_image.html', {'form': form})


@login_required
def update_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/home')
        else:
            return render(request, 'update_profile.html', {'form': form})

    else:
        form = PasswordChangeForm(user = request.user)
        return render(request, 'update_profile.html', {'form': form})


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = UpdationForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/home')
        else:
            return render(request, 'update_profile.html', {'form': form})

    else:
        form = UpdationForm(instance = request.user)
        return render(request, 'update_profile.html', {'form': form})
