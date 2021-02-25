from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
