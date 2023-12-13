import os
from django.db import models

from django.utils.deconstruct import deconstructible

from myapp.models import User

@deconstructible
class GenerateProfileImagePath(object):
    
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f'accounts/{instance.user.id}/images/'
        name = f'profile_image.{ext}'
        return os.path.join(path, name)

user_profile_image_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}\'s Profile'