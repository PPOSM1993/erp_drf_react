from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

from apps.companies.models import Enterprise

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class Groups(models.Model):
    name = models.CharField(max_length=85)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

class GroupsPermissions(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    permission  = models.ForeignKey(Permission, on_delete=models.CASCADE)

class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)