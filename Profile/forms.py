from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']

class ProfileUpdateform(ModelForm):
	labels={
            'profile_pic':'รูปโปรไฟล์',}
	class Meta:
		model = Profile
		fields=['profile_pic']
