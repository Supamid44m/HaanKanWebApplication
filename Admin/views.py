from django.shortcuts import render,redirect
from Party.models import *
from django.contrib import messages
from .forms import *
# Create your views here.

def showuser(req):
    
    return render(req,"Admin/showmember.html",)

def approveParty(req):
    context=Party.objects.all()
    if req.user.is_superuser:
        if req.method=="POST":
             id_list=req.POST.getlist('boxes')
             context.update(isApproved=False)

             for i in id_list:
                Party.objects.filter(pk=int(i)).update(isApproved=True)
             messages.success(req,("อัปเดต"))
             return redirect('party')
        
        else:
            return render(req,"Admin/approveparty.html",{
                'partys':Party.objects.all(),
                'partyapprove':Party.objects.filter(isApproved=True),
                'partyunapprove':Party.objects.filter(isApproved=False)
            })
    else:
        messages.success(req,("คุณไม่มีสิทธ์เข้าถึง"))
        return redirect('party')
    return render(req,"Admin/approveparty.html")
    
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