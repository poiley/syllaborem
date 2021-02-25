from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def __str__(self):
        return 'User {username}'.format(username=self.username)
