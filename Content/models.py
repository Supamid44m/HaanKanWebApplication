from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import *
from django.urls import reverse
from Party.models import Apps
from django.conf import settings


class News(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='Newsimages',null=True,)
    desciption=models.TextField(max_length=500)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_news', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_news', blank=True)
    like_status = models.CharField(max_length=10, default='neutral')



    def like_news(self, user):
        self.likes.add(user)
        self.dislikes.remove(user)
        self.like_status = 'like'
        self.save()

    def unlike_news(self, user):
        self.likes.remove(user)
        self.like_status = 'neutral'
        self.save()
    
    def like_count(self):
        return self.likes.count()
    
    
    def dislike_news(self, user):
        self.dislikes.add(user)
        self.likes.remove(user)
        self.like_status = 'dislike'
        self.save()
    
    def dislike_count(self):
        return self.dislikes.count()
        
    def undislike_news(self, user):
        self.dislikes.remove(user)
        self.like_status = 'neutral'
        self.save()

    def delete_news(self):
        self.delete()
        
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):      
        return reverse('news_detail', kwargs={"id":self.id})
    
