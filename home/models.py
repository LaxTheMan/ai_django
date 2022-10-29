from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class dataModel(models.Model):
    fname = models.fields.CharField(max_length=50, default='a')
    lname = models.fields.CharField(max_length=50, default='a')
    phone = models.fields.IntegerField(default=0)
    img = models.ImageField(upload_to='images/', default=None)


# Create your models here.
