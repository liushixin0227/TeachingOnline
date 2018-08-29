from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
from django.views.generic.base import View

from user.forms import LoginForm, RegisterForm
from user.models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    @staticmethod
    def get(request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    @staticmethod
    def post(request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password','')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()


class LoginView(View):
    @staticmethod
    def get(request):
        return render(request, 'login.html', {})

    @staticmethod
    def post(request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = auth.authenticate(username=user_name, password=pass_word)
            if user is not None:
                auth.login(request, user)
                return render(request, 'index.html', {'msg': '账号或密码错误!'})
        else:
            return render(request, 'login.html', {'login_form': login_form})
