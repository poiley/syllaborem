from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
    
    def __str__(self):
        return 'User {username}'.format(username=self.username)
