from django.shortcuts import render
from .models import User
from django.contrib import messages

def index(req):
    return render(req, 'log_reg/index.html')

def register(req):
    reg_check = User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirm'])

    if reg_check == False:
        return redirect('/')
    else:
        return redirect('/success')




def login(req):

    login_check = User.objects.login(request.POST['log-email'], request.POST['log-password'])

    if login_check == False:
        return redirect('/')
    else:
        return redirect('/success')

def success(req):

    return render(req, 'log_red/success.html')
