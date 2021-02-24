from django.urls import path, include
from django.conf import settings
from apps.user import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]
