from django.urls import path
from catnew.views import MainView, FullArticleView, SignUpView, SignInView, AddArticleView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path('article_page/<int:id>/', FullArticleView.as_view(), name='article_page'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('sign-in/', SignInView.as_view(), name='signin'),
    path('add_article/', AddArticleView.as_view(), name='add_article'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
