from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Message)
admin.site.register(models.Profile)
admin.site.register(models.Conversation)
admin.site.register(models.Devices)