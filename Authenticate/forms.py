from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
	style='bg-gray-50 border border-gray-300 text-zinc-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-grey-300 dark:border-gray-600 dark:placeholder-gray-400 dark:text-zinc-900 dark:focus:ring-zinc-500 dark:focus:border-zinc-500 mb-4'
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':style}))
	first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':style}))
	last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':style})) 

	class Meta(UserCreationForm.Meta):
		model= User
		fields = ('email','first_name','last_name',"username",'password1','password2')
	
	def __init__(self,*args,**kwargs):
		super(RegisterForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class']=self.style
		self.fields['password1'].widget.attrs['class']=self.style
		self.fields['password2'].widget.attrs['class']=self.style


class PasswordChangeForm(PasswordChangeForm):
	style='bg-gray-50 border border-gray-300 text-zinc-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-grey-300 dark:border-gray-600 dark:placeholder-gray-400 dark:text-zinc-900 dark:focus:ring-zinc-500 dark:focus:border-zinc-500'
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':style}),label='รหัสผ่านปัจจุบัน') 
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':style}),label='รหัสผ่านใหม่') 
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':style}),label='ยืนยันรหัสผ่านใหม่') 
	class Meta:
		model=User
		fields = ['old_password','new_password1','new_password2']
		labels = {
            'old_password': 'Current Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm Password'
        }

