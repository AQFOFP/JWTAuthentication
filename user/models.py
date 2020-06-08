from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
