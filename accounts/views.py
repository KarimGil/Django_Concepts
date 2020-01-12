from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def welcome(request):
     return render(request,'welcome.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("welcome")
        else:
            messages.info(request,'Incorect username or password')
            return redirect('login.html')


    else:
        return render(request,'login.html')




def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email)
            user.save()
            print('user created')
            return redirect("/")
    else:
        return render(request,'register.html')
