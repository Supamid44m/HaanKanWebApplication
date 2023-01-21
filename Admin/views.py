from django.shortcuts import render,redirect, get_object_or_404
from Party.models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import get_user_model

# Create your views here.

def showuser(req):
    if req.user.is_superuser:
        User = get_user_model()
        users = User.objects.all()
        return render(req,"Admin/showmember.html",{'users': users})
    else:
        messages.success(req,("คุณไม่มีสิทธ์เข้าถึง"))
        return redirect('party')

def approveParty(req):
    
    if req.user.is_superuser:
        return render(req,"Admin/approveparty.html",{
                'partys':Party.objects.all(),
                'partyapprove':Party.objects.filter(isApproved=True),
                'partyunapprove':Party.objects.filter(isApproved=False)
            })
    else:
        messages.success(req,("คุณไม่มีสิทธ์เข้าถึง"))
        return redirect('party')
    return render(req,"Admin/approveparty.html")

def approve_party(req, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.approve()
    return redirect('/party/')

def reject_party(req, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.reject()
    return redirect('/party/')

def delte_party(req,party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.delete()
    return redirect('/party/')
    
def addApps(req):
    if req.method == 'POST':
        form = AddnewAppforms(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            print("yes")
            return redirect('/')
            
    else:
        form=AddnewAppforms()
        
    context={'form':form}
    return render(req,'Admin/addnewapp.html',context)

def writeNews(req):
    if req.method == 'POST':
        form = WriteNewsforms(req.POST,req.FILES)
        if form.is_valid():
            writer=form.save()
            writer.writer = req.user
            writer.save()
            return redirect('/')
    else:
        form=WriteNewsforms()
        
    context={'form':form}
    return render(req,'Admin/writenews.html',context)

