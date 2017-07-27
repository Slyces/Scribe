from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# =============================================================================
# Extra informations extending the default user model of Django
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id = models.CharField(null=True, blank=True, max_length=20)
    phone_number = models.CharField(null=True, blank=True, unique=True, max_length=10)


# -------------------------------------------------------------------
# Extra work for default users extension

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# =============================================================================
class Conversation(models.Model):
    user = models.ManyToManyField(User)
    nickname = models.CharField(default="John Doe", max_length=20)


# =============================================================================
class Devices(models.Model):
    name = models.CharField(max_length=20)

# =============================================================================
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField()
    device = models.ForeignKey(Devices, null=True)
    contains_special = models.BooleanField(default=False)