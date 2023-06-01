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
    if req.user.is_authenticated:
      user = req.user
      profile = user.profile
      if req.method == "POST":
        userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
        profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=profile)
        if  userform.is_valid()  and profileform.is_valid():
            userform.save()
            profileform.save()
          
            return redirect('/profile/'+str(req.user.id))
      else:
        userform=UserUpdateForm(req.POST or None, req.FILES or None,instance=user)
        profileform=ProfileUpdateform(req.POST or None, req.FILES or None,instance=profile)
      context = {
          'user_form':  userform,
          'profile_form': profileform,
          
      }
      
      return render(req,'Profile/editeprofile.html',context)
    else:
      messages.success(req,("กรุณาเข้าสู่ระบบ"))
      return redirect('party')

def like_profile(req,user_id,):
    if req.user.is_authenticated:
      profile = get_object_or_404(Profile, id=user_id)
      profile.like_profile(req.user)
      return redirect("/profile/"+ str(profile.user.id))
    else:
      messages.success(req,("กรุณาเข้าสู่ระบบ"))
      return redirect('party')


def unlike_profile(req,user_id):
    if req.user.is_authenticated:
      profile = get_object_or_404(Profile, id=user_id)
      profile.unlike_profile(req.user)
      return redirect("/profile/"+ str(profile.user.id))
    else:
      messages.success(req,("กรุณาเข้าสู่ระบบ"))
      return redirect('party')


def dislike_profile(req,user_id):
    if req.user.is_authenticated:
      profile = get_object_or_404(Profile, id=user_id)
      profile.dislike_profile(req.user)
      return redirect("/profile/"+ str(profile.user.id))
    else:
      messages.success(req,("กรุณาเข้าสู่ระบบ"))
      return redirect('party')


def undislike_profile(req,user_id):
    if req.user.is_authenticated:
      profile = get_object_or_404(Profile, id=user_id)
      profile.undislike_profile(req.user)
      return redirect("/profile/"+ str(profile.user.id))
    else:
      messages.success(req,("กรุณาเข้าสู่ระบบ"))
      return redirect('party')

