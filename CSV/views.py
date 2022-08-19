from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UploadFileFormCSV
from django_project.settings import MEDIA_ROOT
# import PyPDF2
# from PyPDF2 import PdfFileReader
# import sys
# import os
# from camelot.core import TABLE_AREA_PADDING
# import csv
# from camelot.parsers import lattice
# import camelot as tableman
# from camelot import *
# import ghostscript





def CSVrip(request):
  if request.method  == "POST":
    form = UploadFileFormCSV(request.POST, request.FILES)
    #x=0
    if form.is_valid():
        #print(os.listdir('/home/runner/djangobytut/media/images/')[0])
        print('1')
        #file = form.save(commit = False)
        form.save()
        #PDF = request.POST.get('image')
        # PDF=open(MEDIA_ROOT+'/PDF/'+
        #                 os.listdir(MEDIA_ROOT+'/PDF/')[0])
        # zz=open(PDF,"rb")
        # pdf_reader = PdfFileReader(zz)
        # Pagenum = pdf_reader.numPages
        # print(Pagenum)


        # x=0
        # #the loop
        # while x!=Pagenum:
        
        #   #increases the iteration
        #   x = x+1
        #   #print("added 1 to x")
        #   #print("loop"+str(x))
        
        #   table = tableman.read_pdf(name2, pages=str(x),flavor='stream',table_areas=['45,1300,425,35'],
        #                             columns=['72,120,220,350,500'],row_tol=12)
        #   table
        #   table.export(name+str(x)+".csv", f=csv , compress=True)
        #   table[0]
        #   table[0].parsing_report
        #   table[0].to_csv(name+str(x)+".csv")
        
      


        messages.success(request, ('Conversion Success'))
        return redirect('Navigation')
        # Redirect to a success page.
        
    else:
        print('2')
        messages.success(request, ('There was an Error in Conversion'))
        return redirect('CSVrip')
        # Return an 'invalid login' error message.
        
  else:
    formv = UploadFileFormCSV
    return render(request, 'CSVRipper.html'
                 , {'form': formv}
                 )
