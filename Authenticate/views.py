from django.shortcuts import render,redirect
from Authenticate.models import *
from django.http import HttpRequest ,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth import login as auth_login ,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Profile.models import Profile

# Create your views here.


def login_user(req):
    if req.user.is_authenticated:
        return redirect("/party/")
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            auth_login(req, user)
            return redirect("/party/")
        else:
            messages.success(req,("ไม่สามารถเข้าสู่ระบบได้กรุณาลองอีกครั้ง"))
            return redirect('login_user')
    
    else:
        return render(req,"Authenticate/login.html",{})



def register(req):
    if req.user.is_authenticated:
        return redirect("/party/")
    if req.method == "POST":
        form=RegisterForm(req.POST)
        if form.is_valid():
            user=form.save()
            profile = Profile(user=user)
            profile.save()
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            auth_login(req, user)
            return redirect('/party/')
    else:
        form=RegisterForm()

    context={"form":form}
    return render(req,"Authenticate/register.html",context)


def change_password(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = PasswordChangeForm(req.user, req.POST)
            if form.is_valid():
                user = form.save()
                messages.success(req, 'Your password was successfully updated!')
                return redirect('/party/')
            else:
                messages.error(req, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(req.user)
        return render(req, 'Authenticate/changepassword.html', {'form': form})
    else:
        return redirect('/party/')


