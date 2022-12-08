from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Party.models import *
from .forms import *
# Create your views here.

def showParty(req):
    context={"party":Party.objects.all()}
    return render(req,'Party/party.html',context)


def crateParty(req):
    if req.method == "POST":
        form=cratePartyforms(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=cratePartyforms()
    context={'form':form}
    return render(req,'Party/createParty.html',context)
