from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages
from .models import Users
from users.additional_funcs.get_data import get_all_nicknames, get_all_emails, hide_email
from users.additional_funcs.pwd_actions import hash_password, check_password
from django.http.response import HttpResponse
import time


class MainView(View):

    def get(self, request):
        users = Users.objects.values_list('email', flat=True)
        users_count = len(users)
        hidden_email = hide_email(users)
        return render(request, 'main.html', {'count': users_count, 'hidden_emails': hidden_email})


class RegistrationView(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        email = request.POST['email'].lower()
        password = request.POST['password']
        password_2 = request.POST['password_2']
        nickname = request.POST['nickname']

        used_email = get_all_emails()
        used_nickname = get_all_nicknames()

        if email and nickname and email not in used_email and nickname not in used_nickname and password == password_2:
            hashed_password = hash_password(password_2)
            user = Users(nickname=nickname, email=email, password=hashed_password)
            user.save()
            time.sleep(5)
            messages.success(request, 'Регистрация успешна 😏')
            return redirect('main')
        if email in used_email or nickname in used_nickname:
            messages.error(request, 'Ошибка! Такая почта или никнейм уже используются 🤣')
        if password != password_2:
            messages.error(request, 'Проверьте правильность введённого пароля и попробуйте ещё раз 😂')

        return render(request, 'signup.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Users.objects.get(email=email)
        except Exception:
            messages.success(request, 'Такого аккаунта не существует')

        else:
            check_pw = check_password(password, user.password)

            if email and check_pw:
                messages.success(request, 'Вы вошли в аккаунт')

                return redirect('main')
            else:
                messages.error(request, 'Похоже, вы ввели неправильный пароль. Попробуйте ещё раз!')

        return render(request, 'login.html')
