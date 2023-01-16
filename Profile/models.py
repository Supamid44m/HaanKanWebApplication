from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,upload_to="images/profliepic")

    def __str__(self):
        return str(self.user)
    
   
