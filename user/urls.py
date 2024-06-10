from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user.forms import LoginForm

from . import views

urlpatterns=[
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='users-register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


