from django.shortcuts import render,redirect
from Party.models import *
from django.contrib import messages
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
            return render(req,"Admin/approveparty.html",{'partys':Party.objects.all()})
    else:
        messages.success(req,("คุณไม่มีสิทธ์เข้าถึง"))
        return redirect('party')
    return render(req,"Admin/approveparty.html")
    