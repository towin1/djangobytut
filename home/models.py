from django.db import models
from django.db.models.fields.files import *

# Create your models here.
#python manage.py makemigrations
#python manage.py migrate

class Member(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  passwd =models.CharField(max_length=100)
  age =models.IntegerField()

  def __str__(self):
    return self.fname+' '+self.lname








class Pic(models.Model):
    imagefile = models.ImageField(null=True, blank=True, upload_to='images/')

    
  


# class PDF(models.Model):
#     imagefile = models.FileField(upload_to='PDF/')

    