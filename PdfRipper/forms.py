from django import forms
from django.forms import ModelForm
from home.models import Pic

class UploadFileForm(ModelForm):
    class Meta:
      model = Pic
      fields = ['imagefile']
      labels = {'imagefile':''}  
     