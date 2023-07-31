from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        confirm_password = request.POST['re_password']

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "username already exists, please change it!.")
            print("username already exists")

        elif password != confirm_password:
            messages.add_message(request, messages.ERROR, "password didn't match")
            print("password invalid")

        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'you are registerd !')
            return redirect('bank_security:login')

    return render(request, 'register.html')


def log_in(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        print(user)
        #
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "welcome {}...".format(user_name))
            return redirect('bank_security:home')

        else:
            messages.add_message(request, messages.ERROR, "invalid username or password!")
            return redirect('bank_security:login')
    return render(request, 'login.html')


def log_out(request):
    auth.logout(request)
    return redirect('/')
