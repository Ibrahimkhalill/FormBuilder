from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as khalil ,logout, authenticate

# Create your views here.
def home(request):
     return render(request,"user/home.html")

def Signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username=request.POST.get('username')     
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if str(pass1) == str(pass2):
            user_object = User(first_name=fname, last_name=lname, username=username)
            user_object.set_password(pass1)
            user_object.save()

            return redirect('login')
        else:
            messages.error(request, 'Both Passwords did not match!')
            return render(request, 'webAi/signup.html')
    return render(request,"user/signup.html")  

def Login(request):
     if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            khalil(request, user)
            return redirect('home')
        else:
             messages.info(request, 'Username OR password is incorrect')
    
    
     return render(request,"user/login.html")