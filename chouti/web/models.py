from django.db import models

# Create your models here.

class SendMsg(models.Model):

    nid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6)
    email = models.CharField(max_length=32, db_index=True)
    times = models.IntegerField(default=0)
    ctime = models.DateTimeField()


class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField()
