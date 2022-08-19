from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from camelot.parsers import lattice
# import PyPDF2
# from PyPDF2 import PdfFileReader
# from PIL import Image 
# import sys
from .forms import UploadFileForm
# import os
# #import csv
# from pytesseract import *
# maxInt = sys.maxsize

# import ghostscript





def PDFRIp(request):
  if request.method  == "POST":
    form = UploadFileForm(request.POST, request.FILES)
    #x=0
    if form.is_valid():
        #print(os.listdir('/home/runner/djangobytut/media/images/')[0])
        print('1')
        #file = form.save(commit = False)
        form.save()
        #PDF = request.POST.get('image')
        # img=Image.open('/home/runner/djangobytut/media/images/'+
        #                os.listdir('/home/runner/djangobytut/media/images/')[0])
        # extractedInformation = pytesseract.image_to_string(img)
        # # txt = tool.image_to_string(
        # #   Image.open('/home/runner/djangobytut/media/images/'
        # #                    +os.listdir('/home/runner/djangobytut/media/images/')[0]),
        # #   lang=lang,
        # #   builder=pyocr.builders.TextBuilder())

        # # print(txt)

        messages.success(request, ('Conversion Success'))
        return redirect('Navigation')
        # Redirect to a success page.
        
    else:
        print('2')
        messages.success(request, ('There was an Error in Conversion'))
        return redirect('PDFRIp')
        # Return an 'invalid login' error message.
        
  else:
    formv = UploadFileForm
    return render(request, 'PdfRipper.html'
                 , {'form': formv}
                 )
