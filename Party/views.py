from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Party.models import *
from .forms import *
from django.views.generic.detail import DetailView
from .models import Party , ChatMessage
from django.contrib.auth.decorators import login_required

# Create your views here.

def showParty(req):
    context={"party":Party.objects.all()}
    return render(req,'Party/party.html',context)


def crateParty(req):
    if req.method == "POST":
        form=cratePartyforms(req.POST,req.FILES)
        if form.is_valid():
            owner=form.save(commit=False)
            owner.owner = req.user
            owner.save()
            form.save_m2m()   
            owner.members.add(req.user)
            return redirect('/')
    else:
        form=cratePartyforms()
    context={'form':form}
    return render(req,'Party/createParty.html',context)


"""@login_required

def party_chat(request, party_id):
    party = Party.objects.get(id=party_id)
    messages = Message.objects.filter(party=party)

    if request.method == 'POST':
        message = request.POST.get('message')
        sender = request.user
        Message.objects.create(content=message, sender=sender, party=party)

    return render(request, 'party_chat.html', {'party': party, 'messages': messages})

"""
def partyDetail(req,id):
    party = get_object_or_404(Party, id=id)
    return render(req,'Party/party_details.html', {'party': party})


def join(req, id):
    party = get_object_or_404(Party, pk= id)
    if req.method == 'POST':
        party.pending_members.add(req.user)
        party.save()
        return redirect('/' + str(id) )
    else:
        return render(req, 'Party/party.html', {'partys': party})

def leave(req, id):
    party = get_object_or_404(Party, pk= id)
    if req.method == 'POST':
        party.leave_party(req.user)
        return redirect('/')
    else:
        return render(req, 'Party/party.html', {'partys': party})

def accept_member(req, party_id, user_id):
    party = Party.objects.get(id=party_id)
    user = User.objects.get(id=user_id)
    if req.user == party.owner:
        party.accept_member(user)
        return redirect("/"+ str(party_id))
    else:
        return redirect("/")

def reject_member(req, party_id, user_id):
    party = Party.objects.get(id=party_id)
    user = User.objects.get(id=user_id)
    if req.user == party.owner:
        party.reject_member(user)
        return redirect("/"+ str(party_id))
    else:
        return redirect("/")

def update_party(req,id):
    party = Party.objects.get(id=id)
    form=cratePartyforms(req.POST or None ,req.FILES or None,instance=party)
    if form.is_valid():
            form.save()   
            return redirect('/')
    return render(req,'Party/updateParty.html',{'partys':party,'form':form})



