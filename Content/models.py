from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=500)
    desciption=models.TextField(max_length=500)
    def __str__(self):
        return self.title 
    




