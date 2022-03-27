from distutils.archive_util import make_archive
from django.db import models

# Create your models here.

class Shop(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop'


class Sword(models.Model):
    sword_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    level = models.IntegerField()
    pic = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'sword'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=128)
    pw = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    money = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'user'

class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level = models.IntegerField()
    upgrade_price = models.IntegerField()
    sell_price = models.IntegerField()
    percentage = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'level'

class UserSword(models.Model):
    user_sword_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    sword_name = models.CharField(max_length=128)
    sword_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_sword'