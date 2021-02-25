from django.urls import path, include
from django.conf import settings
from apps.user import views
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^oauth/", include("social_django.urls")),
    url(r"^register/", views.register, name="register"),
]
