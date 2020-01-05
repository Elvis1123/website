from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/music')
        else:
            messages.info(request,'Invalid entrance')
            return redirect('/music/accounts/login')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        messages.info(request, 'User created')
        return redirect('/music/accounts/login')

    else:
        return render(request, 'register.html')
