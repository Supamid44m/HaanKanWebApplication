from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,upload_to="images/profliepic",blank=True)
    bio=models.TextField(null=True,blank=True,default="")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_profile', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_profile', blank=True)
    like_status = models.CharField(max_length=10, default='neutral')

    def __str__(self):
        return str(self.user)
    
    def like_profile(self, user):
        self.likes.add(user)
        self.dislikes.remove(user)
        self.like_status = 'like'
        self.save()

    def unlike_profile(self, user):
        self.likes.remove(user)
        self.like_status = 'neutral'
        self.save()
    
    def like_count(self):
        return self.likes.count()
    
    
    def dislike_profile(self, user):
        self.dislikes.add(user)
        self.likes.remove(user)
        self.like_status = 'dislike'
        self.save()
    
    def dislike_count(self):
        return self.dislikes.count()
        
    def undislike_profile(self, user):
        self.dislikes.remove(user)
        self.like_status = 'neutral'
        self.save()
    
   
