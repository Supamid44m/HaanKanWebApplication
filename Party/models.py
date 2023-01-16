from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete
from django.dispatch import receiver

   

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
    #owner=models.CharField(max_length=500,null=True)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name='owner')
    members=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    pending_members = models.ManyToManyField(User, related_name="pending_member")
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
    
    def add_membesr(self,user):
        if not user in self.members.all():
            self.members.add(user)
    
    def accept_member(self, user):
        self.pending_members.remove(user)
        self.members.add(user)
    
    def reject_member(self, user):
        self.pending_members.remove(user)
    
    def transfer_owner(self, new_owner):
        self.owner = new_owner
        self.save()

    def leave_party(self, user):
        if user == self.owner:
            new_owner = self.members.exclude(pk=user.pk).first()
            self.transfer_owner(new_owner)
        self.members.remove(user) 
    
from django.db import models

class ChatMessage(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



