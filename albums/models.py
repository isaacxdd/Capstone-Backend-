from django.db import models

# Create your models here.
class Album(models.Model):
    date = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    hotel = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)