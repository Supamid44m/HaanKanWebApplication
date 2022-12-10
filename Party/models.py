from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse



   

class Apps(models.Model):
    name=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to='Appimage',null=True)
    def __str__(self):
        return self.name

class Banks(models.Model):
    name=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name
'''
class Partymember(models.Model):
    fname=models.CharField(max_length=500,null=True)
    lname=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.fname
'''

# Create your models here.
class Party(models.Model):
    owner=models.CharField(max_length=500,null=True)
    members=models.ManyToManyField(User,null=False)
    title = models.CharField(max_length=500,null=False)
    apps = models.ForeignKey(Apps, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True)
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE,null=True)
    bankaccount= models.CharField(max_length=500,null=True)
    qrcodeImage=models.ImageField(upload_to='Partyqrcode',null=True)
    isApproved=models.BooleanField('Approved',default=False)
    price = models.IntegerField(default=0,null=False)

    def __str__(self):
        return self.title 
    
    def priceavg(self):
        return self.price / self.quantity
    
    def get_absolute_url(self):      
        return reverse('partydetails', kwargs={"id":self.id})




