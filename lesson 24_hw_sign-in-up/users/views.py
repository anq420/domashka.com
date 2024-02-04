from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages
from .models import Users
from users.additional_funcs.get_data import (
    get_all_nicknames,
    get_all_emails,
    EmailService,
)
from users.additional_funcs.pwd_actions import hash_password, check_password
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class MainView(View):
    def get(self, request):
        users = Users.objects.values_list("email", flat=True)
        users_count = len(users)
        hidden_email = EmailService.hide(users)
        return render(
            request, "main.html", {"count": users_count, "hidden_emails": hidden_email}
        )


class RegistrationView(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        email = request.POST["email"].lower()
        password = request.POST["password"]
        password_2 = request.POST["password_2"]
        nickname = request.POST["nickname"]

        user = Users.objects.filter(Q(email=email) | Q(nickname=nickname))

        if not user and password == password_2:
            hashed_password = hash_password(password_2)
            user = Users(nickname=nickname, email=email, password=hashed_password)
            user.save()
            messages.success(request, "Регистрация успешна 😏")
            return redirect("main")
        if user:
            messages.error(request, "Ошибка! Такая почта или никнейм уже используются 🤣")
        if password != password_2:
            messages.error(request, "Проверьте правильность введённого пароля и попробуйте ещё раз 😂")

        return render(request, "signup.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = Users.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.error(request, "Такого аккаунта не существует")

        else:
            check_pw = check_password(password, user.password)

            if email and check_pw:
                messages.success(request, "Вы вошли в аккаунт")
                return redirect("main")
            else:
                messages.error(request, "Похоже, вы ввели неправильный пароль. Попробуйте ещё раз!")

        return render(request, "login.html")
