from django.db import models
from django.contrib.auth.models import User

class Pic(models.Model):

    name = models.CharField('FileName', max_length=120)
    imagefile = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
      return self.fname+' '+self.lname
  
  
