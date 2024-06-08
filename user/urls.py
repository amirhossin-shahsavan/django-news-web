from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

