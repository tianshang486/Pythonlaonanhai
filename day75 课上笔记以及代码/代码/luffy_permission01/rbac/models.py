from django.db import models

# Create your models here.

class Userinfo(models.Model):

    name = models.CharField(max_length=12)
    password = models.CharField(max_length=32)
    roles = models.ManyToManyField(to='Role')
    def __str__(self):
        return self.name
class Role(models.Model):
    name = models.CharField(max_length=12)
    permissions = models.ManyToManyField(to='Permission')
    def __str__(self):
        return self.name
class Permission(models.Model):

    url = models.CharField(max_length=32)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title








