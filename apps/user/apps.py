from django.apps import AppConfig

class UserConfig(AppConfig):
    name = 'apps.user'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
