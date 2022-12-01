from django.http.response import HttpResponse
from django.shortcuts import render
from Party.models import *
from .forms import *
# Create your views here.

def showParty(req):
    context={"party":Party.objects.all()}
    return render(req,'Party/party.html',context)


def crateParty(req):
    form=cratePartyforms(req.POST or None)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(req,'Party/createParty.html',context)
