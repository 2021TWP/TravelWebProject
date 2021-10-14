from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountInfo(AbstractUser):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.username

