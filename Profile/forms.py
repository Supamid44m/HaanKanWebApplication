from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']
		
		style='bg-gray-50 border border-gray-300 text-zinc-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-grey-300 dark:border-gray-600 dark:placeholder-gray-400 dark:text-zinc-900 dark:focus:ring-zinc-500 dark:focus:border-zinc-500'
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
		fields=['profile_pic','bio']
		style='bg-gray-50 border border-gray-300 text-zinc-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-grey-300 dark:border-gray-600 dark:placeholder-gray-400 dark:text-zinc-900 dark:focus:ring-zinc-500 dark:focus:border-zinc-500'
		labels={
            'profile_pic':'รูปโปรไฟล์',}
		widgets={
			'profile_pic':forms.FileInput(attrs={'class':"block w-full text-sm text-zinc-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-grey-300 dark:border-gray-600 dark:placeholder-gray-400",}),
			'bio':forms.Textarea(attrs={'class':style}),

        }
