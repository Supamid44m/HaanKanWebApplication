from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import *



class News(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='Newsimages',null=True)
    desciption=models.TextField(max_length=500)
    
    def __str__(self):
        return self.title 
    