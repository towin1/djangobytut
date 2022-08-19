from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
import datetime
from .models import Member
from .forms import MemberForm
from django.contrib import messages


def index(request):
  allmembers = Member.objects.all
  return render(request, 'index.html', {'all':allmembers})

def join(request):
  if request.method == "POST":
    form = MemberForm(request.POST or None)
    if form.is_valid():
      print('worked')
      form.save()
    else:
      fname = request.POST['fname']
      lname = request.POST['lname']
      age = request.POST['age']
      email = request.POST['email']
      passwd = request.POST['passwd']
      messages.success(request, ('There Was An Error In Your Form'))
      return render(request, 'join.html',{'fname':fname,
                                         'lname':lname,
                                         'age':age,
                                         'email':email,
                                         'passwd':passwd})
    messages.success(request, ('Your Form Has Been Submitted Successfully'))
    return redirect('index')
  else:
    return render(request, 'join.html',{})









# def login(request):
#   allmembers = Member.objects.all
#   if request.method == "POST":
#     form = MemberForm(request.POST or None)
#     if form.is_valid():
#       print("``````````````````````````````````````````````````````````````````````````````````````````````")
#       #form.save()
#     else:
#       messages.success(request, ('Either Your Login Or Your Password Was Incorrect'))
#       return render(request, 'login.html')
#     messages.success(request, ('Login Successful'))
#     return redirect('index')
#   else:
#     return render(request, 'login.html', {'all':allmembers})
















#today = datetime.datetime.now().date()