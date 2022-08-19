from django import forms
from django.forms import ModelForm
from .models import Pdf

class UploadFileFormCSV(ModelForm):
    class Meta:
      model = Pdf
      fields = ['PDFfile']
      labels = {'PDFfile':''}  
     