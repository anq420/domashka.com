from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.db.models import Q
from catnew.forms import RegistrationForm
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


class MainView(View):
    def get(self, request):
        all_news = News.objects.all()
        return render(request, 'main_page.html', context={'data': all_news[::-1]})


class AddArticleView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_article.html')

    def post(self, request):
        nickname = request.POST['nickname']
        title = request.POST['title']
        content = request.POST['content']

        article = News(author=nickname, title=title, content=content)
        article.save()

        return render(request, 'add_article.html')


class FullArticleView(View):
    def get(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        context = {'news': news}
        return render(request, 'detailed_article.html', context)


class SignUpView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            user = User.objects.filter(Q(email=email) | Q(username=username))

            if not user and password == confirm_password:
                user_ = User.objects.create_user(email=email, username=username, password=confirm_password)
                user_.save()
                messages.success(request, 'Успешная регистрация')

            if user:
                messages.error(request, 'Такая почта или никнейм уже используются')

            if password != confirm_password:
                messages.error(request, "Проверьте правильность введённого пароля и попробуйте ещё раз")

        return render(request, 'registration.html', {'form': form})


class SignInView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            u_pass = user.check_password(password)

            if user and u_pass:
                login(request, user)
                messages.success(request, 'Успешный вход')
                return redirect('main')
            else:
                messages.error(request, 'Неверный пароль')
        except User.DoesNotExist:
            messages.error(request, 'Пользователь с таким адресом электронной почты не найден')

        return render(request, 'login.html')
