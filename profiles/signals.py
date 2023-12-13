from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from myapp.models import User

from profiles.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
