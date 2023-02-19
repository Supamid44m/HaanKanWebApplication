from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
	style='bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':style}))
	first_name = forms.CharField(max_length=50,widget=forms.TimeInput(attrs={'class':style}))
	last_name = forms.CharField(max_length=50,widget=forms.TimeInput(attrs={'class':style})) 

	class Meta(UserCreationForm.Meta):
		model= User
		fields = ('email','first_name','last_name',"username",'password1','password2')
	
	def __init__(self,*args,**kwargs):
		super(RegisterForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class']=self.style
		self.fields['password1'].widget.attrs['class']=self.style
		self.fields['password2'].widget.attrs['class']=self.style


