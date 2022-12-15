import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models




class User(models.Model):

    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


