from django.urls import path
from users.views import MainView, RegistrationView, LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('sign-up/', RegistrationView.as_view()),
    path('sign-in/', LoginView.as_view())
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)