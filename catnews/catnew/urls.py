from django.urls import path
from catnew.views import MainView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", MainView.as_view(), name="main")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
