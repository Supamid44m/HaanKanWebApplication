from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=500)
    desciption=models.TextField(max_length=500)
    




