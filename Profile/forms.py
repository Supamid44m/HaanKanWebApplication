from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']
		
		style='bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
		widgets={
			'username':forms.TextInput(attrs={'class':style,}),
			'first_name':forms.TextInput(attrs={'class':style,}),
			'last_name':forms.TextInput(attrs={'class':style,}),
			'email':forms.TextInput(attrs={'class':style,}),
           

        }
		help_texts = {
            'username': None,
        }

class ProfileUpdateform(ModelForm):
	
	class Meta:
		model = Profile
		fields=['profile_pic']
		sytle='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
		labels={
            'profile_pic':'รูปโปรไฟล์',}
		widgets={
			'profile_pic':forms.FileInput(attrs={'class':"block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400",}),
           

        }
