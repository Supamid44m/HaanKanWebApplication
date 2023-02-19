from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Party.models import *
from .forms import *
from django.views.generic.detail import DetailView
from .models import Profile
from django.contrib import messages
from .forms import UserUpdateForm,ProfileUpdateform
# Create your views here.

def profiledetail(req,user_id):
  if req.user.is_authenticated:
    profile = Profile.objects.get(user_id=user_id)
    return render(req,'Profile/profile_detail.html',{"profile":profile})
  else:
    messages.success(req,("กรุณาเข้าสู่ระบบ"))
    return redirect('party')



def editprofile(req):
    
    user = req.user
    profile = user.profile
    form = ProfileUpdateform(instance=profile)
    if req.method == "POST":
      userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
      profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=profile)
      if  userform.is_valid()  and profileform.is_valid():
          userform.save()
          profileform.save()
        
          return redirect('/profile/'+str(req.user.id))
    else:
      userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
      profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=req.user)
    context = {
        'user_form':  userform,
        'profile_form': profileform,
    }
     
    return render(req,'Profile/editeprofile.html',context)
