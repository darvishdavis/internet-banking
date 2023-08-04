from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    user = None
    return render(request, 'home.html', dict(user=user))


def register(request):
    user = None
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

        elif not username:
            messages.error(request, 'please enter a username')

        elif not password:
            messages.error(request, 'please enter a strong password')

        elif not confirm_password:
            messages.error(request, 'please retype password')

        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'you are registered !')
            return redirect('bank_security:login')

    return render(request, 'register.html', dict(user=user))


def log_in(request):
    user = None
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        print(user)
        #
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "welcome {}...".format(user_name))
            return redirect('bank_body:new')

        else:
            messages.add_message(request, messages.ERROR, "invalid username or password!")
            return redirect('bank_security:login')
    return render(request, 'login.html', dict(user=user))


def log_out(request):
    auth.logout(request)
    return redirect('/')
