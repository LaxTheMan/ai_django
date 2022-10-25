from django.db import models

class samplemodel(models.Model):
    number = models.IntegerField()
    description = models.TextField()

# Create your models here.
