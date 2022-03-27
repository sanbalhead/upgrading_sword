from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=150, blank=True)
    money =  models.IntegerField(blank=True)

    class Meta:
        managed = False
        db_table = 'user'
