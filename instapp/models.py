from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo= models.ImageField(upload_to='profiles/',null=True)
    bio= models.CharField(max_length=100, null=True)

class Post(models.Model):
    post_image = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(max_length =240)
    location = models.CharField(max_length =30)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True)
    like = models.IntegerField(default=0)

