from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import *
from django.urls import reverse
from Party.models import Apps


class News(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='Newsimages',null=True,)
    desciption=models.TextField(max_length=500)
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):      
        return reverse('news_detail', kwargs={"id":self.id})
    