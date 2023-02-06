from datetime import timezone, date, datetime,timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete
from django.dispatch import receiver
from PIL import Image

   

class Apps(models.Model):
    name=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to='Appimage',null=True)
    isApproved=models.BooleanField('Approved',default=False)


    def approve(self):
        self.isApproved = True
        self.save()

    def reject(self):
        self.delete()

    def handle_approval(self, user):
        if user.is_superuser:
            self.isApproved = True
        else:
            self.isApproved = False
        self.save()

    def __str__(self):
        return self.name

class Banks(models.Model):
    name=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name

# Create your models here.
class Party(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name='owner')
    members=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    pending_members = models.ManyToManyField(User, related_name="pending_member")
    title = models.CharField(max_length=500,null=False)
    apps = models.ForeignKey(Apps, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True)
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE,null=True)
    bankaccount= models.CharField(max_length=500,null=True)
    qrcodeImage = models.ImageField(upload_to='Partyqrcode', null=True, width_field='image_width', height_field='image_height')
    image_width = models.IntegerField(null=True)
    image_height = models.IntegerField(null=True)
    isApproved=models.BooleanField('Approved',default=False)
    price = models.IntegerField(default=0,null=False)
    priceaverage = models.FloatField(default=0.0,null=True,blank=True)
    paid_day = models.IntegerField(default=1,null=False,validators=[MinValueValidator(1), MaxValueValidator(31)])
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_parties', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_parties', blank=True)
    
    like_status = models.CharField(max_length=10, default='neutral')
    
    def like_party(self, user):
        self.likes.add(user)
        self.dislikes.remove(user)
        self.like_status = 'like'
        self.save()

    def unlike_party(self, user):
        self.likes.remove(user)
        self.like_status = 'neutral'
        self.save()
    
    def like_count(self):
        return self.likes.count()
    
    
    def dislike_party(self, user):
        self.dislikes.add(user)
        self.likes.remove(user)
        self.like_status = 'dislike'
        self.save()
    
    def dislike_count(self):
        return self.dislikes.count()
        
    def undislike_party(self, user):
        self.dislikes.remove(user)
        self.like_status = 'neutral'
        self.save()
            
    

    def days_until_paid(self, current_date):
        paid_day = self.paid_day
        current_date = date.fromisoformat(current_date)
        max_day = self.get_max_day(current_date.month, current_date.year)
        if paid_day > max_day:
            paid_day = max_day
        paid_date = date(current_date.year, current_date.month, paid_day)
        if paid_date < current_date:
            paid_date = paid_date.replace(month=paid_date.month + 1)
        difference = paid_date - current_date
        return difference.days

    def get_max_day(self,month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            return 28
        return 30
    
    
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
    
    def delete_members(self,user):
        if user == self.owner:
            new_owner = self.members.exclude(pk=user.pk).first()
            self.transfer_owner(new_owner)
        self.members.remove(user)
        self.save()

    def approve(self):
        self.isApproved = True
        self.save()

    def reject(self):
        self.delete()
    
    
    
    def mask_bankaccount(self):
        return "xxxxxxxx" + self.bankaccount[-2:]
    


class ChatMessage(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class EvidenceimageParty(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='EvidenceimageParty')
    evidenceimage = models.ImageField(upload_to='evidence_of_payment', null=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='uploader')
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)


    def delete_evidence(self, user):
        if self.uploader == user:
            self.delete()
            return True
        else:
            return False
        

