from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.username


class UserGroup(models.Model):
    group_name = models.CharField(max_length=20, blank=False)
    pin = models.CharField(max_length=8, blank=False)

    def __str__(self):
        return self.group_name
