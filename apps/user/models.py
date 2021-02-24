from django.db import models
from django.contrib.auth.models import AbstractUser

<<<<<<< HEAD
# Create your models here.
from django.contrib.auth.models import User as u
class User(u):
=======
class User(AbstractUser):
>>>>>>> b3aa12ca0f428db7b60fdb0548d17c5056a5bb49
    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
    
    def __str__(self):
        return 'User {username}'.format(username=self.username)
