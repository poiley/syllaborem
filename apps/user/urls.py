from django.urls import path, include
from django.conf import settings
from apps.user import views
from apps.user.views import dashboard, register
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    path('', dashboard, name='dashboard'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
]
