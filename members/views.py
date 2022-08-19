from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login_user(request):
  if request.method  == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, ('Login Success'))
        return redirect('Navigation')
        # Redirect to a success page.
        
    else:
      messages.success(request, ('There was an Error Logging in'))
      return redirect('login')
        # Return an 'invalid login' error message.
        
  else:
    return render(request, 'authenticate/login.html', {})




def register_user(request):
  if request.method  == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['passwword1']
      user = authenticate(username=username,password=password)
      login(request,user)
      messages.success(request, ('Login Success'))
      return redirect('Navigation')
  else:
    form = UserCreationForm()
  return render(request, 'authenticate/register_user.html',{'form':form,})



def Navigation(request):
  if request.method  == "POST":
    NAV = request.POST['NAV']
    print(NAV)
    if NAV == 'Logout':
      logout(request)
      return redirect('login')
    else:
      messages.success(request, ('There was an Error Navigating'))
      return redirect('Navigation')
  else:
    return render(request, 'authenticate/Navigation.html')


    