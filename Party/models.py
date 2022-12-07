from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class AppImage(models.Model):
    imgeName=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to=None)
    imageURL=models.CharField(max_length=500)
    def __str__(self):
        return self.imgeName
   

class Apps(models.Model):
    name=models.CharField(max_length=500,null=True)
    appImage=models.ForeignKey(AppImage,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

       
class QrcodePayment(models.Model):
    
    qrcodeImage=models.ImageField(upload_to=None)
    qrcodeImageURL=models.CharField(max_length=500)

# Create your models here.
class Party(models.Model):
    title = models.CharField(max_length=500)
    member=models.ManyToManyField(User,null=True)
    apps = models.ForeignKey(Apps, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    qrcodepayment=models.ForeignKey(QrcodePayment, on_delete=models.CASCADE,null=True)
    isApproved=models.BooleanField('Approved',default=False)
    
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.title 



