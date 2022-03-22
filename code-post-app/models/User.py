from django.db import models
import re
import bcrypt

class User(models.Model):
    username = models.Charfield(max_length=48, unique=True)
    email_address = models.CharField(max_length=320, unique=True)
    password = models.CharField(max_length=64, min_length=8)

    class Meta:
        app_label = 'code-post-app'