from django import forms
from Party.models import Party
from django.forms import ModelForm
from .models import *

class cratePartyforms(ModelForm):
    class Meta:
        model=Party
        fields=('title','apps','quantity','qrcodeImage','price')
        labels={
            'title':'Title',
            'apps':'Apps',
            'quantity':'Quatity',
            'qrcodeImage':'Qrcodepayment',
            'price':'Price',

        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อ'}),
            'apps':forms.Select(attrs={'placeholder':'แอป'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'จำนวน'}),
            'qrcodeImage':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'ช่องทางชำระ'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'ราคา'})

        }