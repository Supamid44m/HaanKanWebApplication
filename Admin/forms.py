from django import forms
from .models import *
from Party.models import Party
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