from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Apps(models.Model):
    name=models.CharField(max_length=500)
    def __str__(self):
        return self.name



# Create your models here.
class Party(models.Model):
    title = models.CharField(max_length=500)
    member=models.ManyToManyField(User,null=True)
    apps = models.ForeignKey(Apps, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    isApproved=models.BooleanField('Approved',default=False)
    
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.title 



