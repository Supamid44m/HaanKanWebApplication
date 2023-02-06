from django import forms
from Party.models import Party,Apps
from django.forms import ModelForm
from .models import *

class cratePartyforms(ModelForm):
    use_priceavg = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','placeholder':'ให้ระบบหารราคาให้'}), required=False,label='ให้เว็บหารราคาให้')
    apps = forms.ModelChoiceField(queryset=Apps.objects.filter(isApproved=True), widget=forms.Select(attrs={'placeholder':'เลือกแอปพลิเคชั่น'}),label='เลือกแอปพลิเคชั่น')
    class Meta:
        model=Party
        fields=('title','apps','quantity','qrcodeImage','bank','bankaccount','price','priceaverage','paid_day')
        labels={
            'title':'ชื่อปาร์ตี้',
            'apps': 'แอปพลิเคชั่น',
            'quantity':'จำนวน (รวมตัวเอง)',
            'qrcodeImage':'Qrcode เพื่อสแกนจ่าย',
            'bank':'ธนาคาร',
            'bankaccount':'เลขบัญชี',
            'price':'ราคาเต็ม',
            'priceaverage':'ราคาเฉลี่ย  / คน',
            'paid_day':'จ่ายทุกวันที่',

        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อ'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'จำนวน'}),
            'bank':forms.Select(attrs={'placeholder':'ธนาคาร'}),
            'bankaccount':forms.TextInput(attrs={'placeholder':'เลขบัญชี'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'ราคา'}),
            'priceaverage':forms.NumberInput(attrs={'class':'form-control','placeholder':'ราคาเฉลี่ย'}),
            'paid_day':forms.NumberInput(attrs={'class':'form-control','placeholder':'จ่ายทุกวันที่'})

        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['apps'].queryset = Apps.objects.filter(isApproved=True)

            
        def priceavg(self):
            return Party.priceavg()

class addMemberForm(ModelForm):
    class Meta:
        models=Party
        fields=('members',)
        labels={'members':'เพิ่มสมาชิก'}
        widgets={
            'members':forms.SelectMultiple(attrs={'placeholder':'เพิ่มสมาชิก'})
        }
    
class AddMemberForms(forms.Form):
    member = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False), empty_label=None)

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = EvidenceimageParty
        fields = ['evidenceimage']

    evidenceimage = forms.ImageField(label='อัปโหลดหลักฐานการโอน')

