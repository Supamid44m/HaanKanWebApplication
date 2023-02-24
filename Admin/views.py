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
    

def approve_party(req, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.approve()
    return redirect('/Admin/approveparty')

def reject_party(req, party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.reject()
    return redirect('/Admin/approveparty')

def delte_party(req,party_id):
    party = get_object_or_404(Party, pk=party_id)
    party.reject()
    return redirect('/Admin/approveparty')
    
def addApps(req):
    app=Apps.objects.all()
    if req.method == 'POST':
        form = AddnewAppforms(req.POST,req.FILES)
        if form.is_valid():
            app=form.save(commit=False)
            app.handle_approval(req.user)
            app.save()
            print("yes")
            return redirect('/app')
            
    else:
        form=AddnewAppforms()

    context={'form':form,'apps':app}
    return render(req,'Admin/addnewapp.html',context)

def showApps(req):
    if req.user.is_superuser:
        app=Apps.objects.all()
        return render(req,'Admin/applist.html',{'apps':app})
    else:
         return redirect('party')

def approve_app(req, app_id):   
    app = get_object_or_404(Apps, pk=app_id)
    app.approve()
    return redirect('/Admin/applist')

def reject_app(req, app_id):
    app = get_object_or_404(Apps, pk=app_id)
    app.reject()
    return redirect('/Admin/applist')

def delete_app(req,app_id):
    if req.user.is_superuser:
        app = get_object_or_404(Apps, pk=app_id)
        app.reject()
        return redirect('/Admin/applist')
    else:
        return redirect('party')


def edit_app(req,app_id):
    app = Apps.objects.get(id=app_id)
    form=AddnewAppforms(req.POST or None ,req.FILES or None,instance=app)
    if form.is_valid():
        form.save()
        messages.success(req,("แก้ไขสำเร็จ"))
        return redirect('/Admin/applist')
        
    return render(req,'Admin/updateApp.html',{'apps':app,'form':form})

def showBanks(req):
    if req.user.is_superuser:
        bank=Banks.objects.all()
        return render(req,'Admin/bankslist.html',{'banks':bank})
    else:
         return redirect('party')

def addBanks(req):
    if req.user.is_superuser:
        bank=Banks.objects.all()
        if req.method == 'POST':
            form = AddbankForms(req.POST,)
            if form.is_valid():
                bank=form.save(commit=False)
                bank.save()
                return redirect('/Admin/addbanks')
        else:
            form=AddbankForms()
    else:
        return redirect('party')

    context={'form':form,'banks':bank}
    return render(req,'Admin/addbanks.html',context)


def delete_bank(req,bank_id):
    if req.user.is_superuser:
        bank = get_object_or_404(Banks, pk=bank_id)
        bank.deletebanks()
        return redirect('/Admin/banklist')
    else:
        return redirect('party')

def edit_bank(req,bank_id):
    if req.user.is_superuser:
        bank = Banks.objects.get(id=bank_id)
        form=AddbankForms(req.POST or None ,req.FILES or None,instance=bank)
        if form.is_valid():
            form.save()
            messages.success(req,("แก้ไขสำเร็จ"))
            return redirect('/Admin/banklist')
            
        return render(req,'Admin/updatebank.html',{'bank':bank,'form':form})
    else:
        return redirect('party')








def writeNews(req):
    if req.method == 'POST':
        form = WriteNewsforms(req.POST,req.FILES)
        if form.is_valid():
            writer=form.save()
            writer.writer = req.user
            writer.save()
            return redirect('/news/')
    else:
        form=WriteNewsforms()
        
    context={'form':form}
    return render(req,'Admin/writenews.html',context)



def editprofile(req,user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    user = profile.user
    
    if req.method == "POST":
      userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
      profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=profile)
      if  userform.is_valid()  and profileform.is_valid():
          userform.save()
          profileform.save()
        
          return redirect('/Admin/alluser')
    else:
      userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
      profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=req.user)
    context = {
        'user_form':  userform,
        'profile_form': profileform,
    }
     
    return render(req,'Profile/editeprofile.html',context)

def delete_user(req,user_id):
    user = get_object_or_404(User,id=user_id)
    if user == req.user:
        return redirect('/Admin/alluser')
    elif  user.is_superuser:
        return redirect('/Admin/alluser')
        
    else:
         user.delete()


