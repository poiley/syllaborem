from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.user.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
