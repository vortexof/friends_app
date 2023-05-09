from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель пользователя
    """
    name = models.CharField(max_length=255, default='')
    surname = models.CharField(max_length=255, default='')

