from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True, verbose_name='аватарка')
    age = models.PositiveSmallIntegerField(default=0, verbose_name='возраст')
