from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



   

class Apps(models.Model):
    name=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to='Appimage',null=True)
    def __str__(self):
        return self.name

       


# Create your models here.
class Party(models.Model):
    title = models.CharField(max_length=500,null=False)
    member=models.ManyToManyField(User,null=True,blank=True)
    apps = models.ForeignKey(Apps, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True)
    qrcodeImage=models.ImageField(upload_to='Partyqrcode',null=True,blank=True)
    isApproved=models.BooleanField('Approved',default=False)
    price = models.IntegerField(default=0,null=False)

    def __str__(self):
        return self.title 



