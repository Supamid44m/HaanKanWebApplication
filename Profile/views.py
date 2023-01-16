from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Party.models import *
from .forms import *
from django.views.generic.detail import DetailView
from .models import Profile
from .forms import UserUpdateForm,ProfileUpdateform
# Create your views here.

def profiledetail(req,id):
    
    return render(req,'Profile/profile_detail.html',
    {
    'profile': get_object_or_404(Profile, pk=id),
    
    }
  )



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
        
          redirect('/')
    else:
      userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
      profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=req.user)
    context = {
        'user_form':  userform,
        'profile_form': profileform,
    }
     
    return render(req,'Profile/editeprofile.html',context)
