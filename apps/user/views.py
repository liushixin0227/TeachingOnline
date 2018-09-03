from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
from django.views.generic.base import View

from user.forms import LoginForm, RegisterForm, ForgetPwdForm
from user.models import UserProfile, EmailVerifyRecord
from utils.email_send import send_register_email


class ActiveUserView(View):
    @staticmethod
    def get(request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(username=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


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
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form,
                                                         'msg': '邮箱已存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


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
                if user.is_active:
                    auth.login(request, user)
                    return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'用户未激活'})
        else:
            return render(request, 'login.html', {'login_form': login_form}, {'msg': '账号或密码错误!'})


class ForgetPwdView(View):
    @staticmethod
    def get(request):
        forgetpwd_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forgetpwd_form': forgetpwd_form})

    @staticmethod
    def post(request):
        forgetpwd_form = ForgetPwdForm(request.POST)
        if forgetpwd_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forgetpwd_form': forgetpwd_form})
