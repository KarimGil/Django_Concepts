from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass']
        user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email)
        user.save()
        print('user created')
        return redirect("/")
    else:
        return render(request,'register.html')
