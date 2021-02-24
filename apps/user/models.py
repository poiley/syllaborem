from django.db import models

# Create your models here.
from django.contrib.auth.models import User as u
class User(u):
    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
    
    def __str__(self):
        return 'User {username}'.format(username=self.username)
