from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(unique=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'User'

class Post(models.Model):
    user = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    heading = models.CharField(max_length=500,blank=False,null=False)
    description = models.CharField(max_length=10000,blank=False,null=False)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False,null=False)

    class Meta:
        db_table = 'Post'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=10000)

    class Meta:
        db_table = 'Comment'