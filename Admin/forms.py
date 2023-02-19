from django import forms
from .models import *
from Party.models import Party,Apps,Banks
from Content.models import News

from django.forms import ModelForm

class ApprovePartyforms(ModelForm):
    class Meta:
        model=Party
        fields=('title','apps','quantity','price','isApproved')
        labels={
            'title':'Title',
            'apps':'Apps',
            'quantity':'Quatity',
            'isApproved':'isApproved',
            'price':'Price',

        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อ'}),
            'apps':forms.Select(attrs={'placeholder':'แอป'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'จำนวน'}),
            'isApproved':forms.CheckboxInput(attrs={'class':'form-control','placeholder':'อนุมัติ'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'ราคา'})

        }

class AddnewAppforms(ModelForm):

    class Meta:
        style='bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        model=Apps
        fields=('name','image')
        labels={
            'name':'ชื่อแอป',
            'image':'รูป',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':style,'placeholder':'ขื่อแอป'}),
            'image': forms.FileInput(attrs={'class':"block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400",'placeholder':'ขื่อแอป'}),
            
        }
class AddbankForms(ModelForm):
    class Meta:
        model=Banks
        style='bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        fields=('name',)
        labels={
            'name':'ชื่อธนาคาร',
            
        }
        widgets={
            'name': forms.TextInput(attrs={'class':style,'placeholder':'ชื่อธนาคาร'}),
           
        }

class WriteNewsforms(ModelForm):
    class Meta:
        model=News
        fields=('title','image','desciption')
        labels={
            'title':'หัวข้อข่าว',
            'image':'Image',
            'desciption':'รายละเอียด'
        }
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'หัวข้อข่าว'}),
            'desciption': forms.Textarea(attrs={'class':'form-control','placeholder':'รายละเอียด'}),
        }


