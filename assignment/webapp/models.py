from django.db import models

# Create your models here.

class RequestCounter(models.Model):
    counter = models.IntegerField(default=0)
