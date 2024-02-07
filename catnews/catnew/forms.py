from django.contrib.auth.forms import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действительный адрес электронной почты.')
    username = forms.CharField(max_length=30, help_text='Обязательное поле. Максимум 30 символов.')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Обязательное поле. Пароль не должен совпадать с вашим никнеймом и состоять менее чем из 8 символов.')
    confirm_password = forms.CharField(widget=forms.PasswordInput, help_text='Обязательное поле. Повторите ввод пароля для подтверждения.')

    class Meta:
        fields = ['email', 'username', 'password', 'confirm_password']
