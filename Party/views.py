from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Party.models import *
from .forms import *
from django.views.generic.detail import DetailView
from .models import Party
# Create your views here.

def showParty(req):
    context={"party":Party.objects.all()}
    return render(req,'Party/party.html',context)


def crateParty(req):
    if req.method == "POST":
        form=cratePartyforms(req.POST,req.FILES)
        if form.is_valid():
            owner=form.save(commit=False)
            owner.owner = str(req.user)  
            owner.save()
            form.save_m2m()   
            owner.members.add(req.user)
            return redirect('/')
    else:
        form=cratePartyforms()
    context={'form':form}
    return render(req,'Party/createParty.html',context)


def partyDetail(req,id):
    return render(req,'Party/party-details.html',
    {
    'party': get_object_or_404(Party, pk=id)
    }
  )


def join(req, id):
    party = get_object_or_404(Party, pk= id)
    if req.method == 'POST':
        party.members.add(req.user)
        party.save()
        return redirect('/' + str(id) )
    else:
        return render(req, 'Party/party.html', {'partys': party})