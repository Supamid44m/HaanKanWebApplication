from django import forms
from Party.models import Party
from django.forms import ModelForm
from .models import *

class cratePartyforms(ModelForm):
    class Meta:
        model=Party
        fields=('title','apps','quantity','qrcodeImage','bank','bankaccount','price','paid_day')
        labels={
            'title':'ชื่อปาร์ตี้',
            'apps':'แอปพลิเคชั่น',
            'quantity':'จำนวน',
            'qrcodeImage':'Qrcode เพื่อสแกนจ่าย',
            'bank':'ธนาคาร',
            'bankaccount':'เลขบัญชี',
            'price':'ราคาเต็ม',
            'paid_day':'จ่ายทุกวันที่',

        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อ'}),
            'apps':forms.Select(attrs={'placeholder':'แอป'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'จำนวน'}),
            'bank':forms.Select(attrs={'placeholder':'ธนาคาร'}),
            'bankaccount':forms.TextInput(attrs={'placeholder':'เลขบัญชี'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'ราคา'}),
            'paid_day':forms.NumberInput(attrs={'class':'form-control','placeholder':'จ่ายทุกวันที่'})

        }

class addMemberForm(ModelForm):
    class Meta:
        models=Party
        fields=('members',)
        labels={'members':'เพิ่มสมาชิก'}
        widgets={
            'members':forms.SelectMultiple(attrs={'placeholder':'เพิ่มสมาชิก'})
        }
    
class AddMemberForms(forms.Form):
    member = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)

