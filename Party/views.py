from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Party.models import *
from .forms import *
from django.views.generic.detail import DetailView
from .models import Party , ChatMessage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime
from django.contrib import messages as msg


# Create your views here.

def showParty(req):
    context={"party":Party.objects.all()}
    return render(req,'Party/party.html',context)

@login_required
def crateParty(req):
    if req.method == "POST":
        form=cratePartyforms(req.POST,req.FILES)
        if form.is_valid():
            use_price_avg = form.cleaned_data.get('use_price_avg')
            if use_price_avg:
                form.priceavg()
            owner=form.save(commit=False)
            owner.owner = req.user
            owner.save()
            form.save_m2m()   
            owner.members.add(req.user)
            return redirect('/party/')
    else:
        form=cratePartyforms()
    context={'form':form}
    return render(req,'Party/createParty.html',context)

def update_party(req,id):
    party = Party.objects.get(id=id)
    form=cratePartyforms(req.POST or None ,req.FILES or None,instance=party)
    if form.is_valid():
        use_price_avg = form.cleaned_data.get('use_price_avg')
        if use_price_avg:
            form.priceavg()
        form.save()   
        return redirect('/party/'+str(id))
    return render(req,'Party/updateParty.html',{'partys':party,'form':form})



"""def partyDetail(req,id):
    party = get_object_or_404(Party, id=id)
    return render(req,'Party/party_details.html', {'party': party})"""

def partyDetail(req,id):
    party = get_object_or_404(Party, id=id)
    current_date = date.today().isoformat()
    messages = ChatMessage.objects.filter(party=party)
    evidence = EvidenceimageParty.objects.filter(party=party)
    days_left = party.days_until_paid(current_date)
    form = None
    upform=EvidenceForm()
    if req.user == party.owner:
        form = AddMemberForms()
    return render(req,'Party/party_details.html', {'party': party, 'messages': messages,'days_left':days_left,"form":form,'evidence':evidence,"upform":upform})




def upload_evidence(request, id):
    party = get_object_or_404(Party, id=id)
    if request.method == 'POST':
        form = EvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            evidence = form.save(commit=False)
            evidence.party = party
            evidence.uploader=request.user
            evidence.save()
    return redirect('/party/' + str(id))
   


def add_member(req,id):
    party = get_object_or_404(Party, id=id)
    if req.user == party.owner and req.method == "POST":
        form = AddMemberForms(req.POST)
        if form.is_valid():
            member = form.cleaned_data['member']
            party.members.add(member)
    return redirect('/party/' + str(id))

def delete_member(req,id,member_id):
    party = get_object_or_404(Party, id=id)
    member = get_object_or_404(User, id=member_id)
    if req.user == party.owner and req.method == "POST":
        party.delete_members(member)
    return redirect('/party/' + str(id))

def join(req, id):
    party = get_object_or_404(Party, pk= id)
    if req.method == 'POST':
        party.pending_members.add(req.user)
        party.save()
        return redirect('/party/' + str(id) )
    else:
        return render(req, 'Party/party.html', {'partys': party})


def delete_party(req,id):
    party = get_object_or_404(Party,pk=id)
    if req.user==party.owner and req.method == "POST":
        party.reject()
        return redirect('/party/')


def leave(req, id):
    party = get_object_or_404(Party, pk= id)
    if req.method == 'POST':
        party.leave_party(req.user)
        return redirect('/party/')
    else:
        return render(req, 'Party/party.html', {'partys': party})

def accept_member(req, party_id, user_id):
    party = Party.objects.get(id=party_id)
    user = User.objects.get(id=user_id)
    if req.user == party.owner:
        party.accept_member(user)
        return redirect("/party/"+ str(party_id))
    else:
        return redirect("/party/")

def reject_member(req, party_id, user_id):
    party = Party.objects.get(id=party_id)
    user = User.objects.get(id=user_id)
    if req.user == party.owner:
        party.reject_member(user)
        return redirect("/party/"+ str(party_id))
    else:
        return redirect("/party/")

def search(req,):
    if req.method == "POST":
        searched= req.POST["searched"]
        party=Party.objects.filter(Q(title__icontains=searched) | Q(price__icontains=searched) | Q(apps__name__icontains=searched))
        return render(req,'Party/searchParty.html',
        {
            'searched':searched,
            'party':party
        })
    else:
        return render(req,'Party/searchParty.html',{})

def like_party(request, party_id):
    user = request.user
    party = get_object_or_404(Party, pk=party_id)
    party.like_party(user)
    return redirect("/party/"+ str(party_id))


def unlike_party(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.unlike_party(request.user)
    return redirect("/party/"+ str(party_id))


def dislike_party(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.dislike_party(request.user)
    return redirect("/party/"+ str(party_id))


def undislike_party(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.undislike_party(request.user)
    return redirect("/party/"+ str(party_id))

def show_evidence(req,id):
    party = get_object_or_404(Party, id=id)
    evidence = EvidenceimageParty.objects.filter(party=party)
    return render(req,'Party/show_evidence.html', {'party': party, 'evidence':evidence,})




