from django.shortcuts import render,redirect
from Authenticate.models import *
from django.http import HttpRequest ,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth import login as auth_login ,authenticate
from django.contrib.auth import logout

# Create your views here.



def register(req):
    if req.method == "POST":
        form=RegisterForm(req.POST)
        if form.is_valid():
            user=form.save()
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            auth_login(req, user)
            return redirect('/')
    else:
        form=RegisterForm()

    context={"form":form}
    return render(req,"Authenticate/register.html",context)
