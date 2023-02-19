from django import forms
from Party.models import Party,Apps
from django.forms import ModelForm
from .models import *

class cratePartyforms(ModelForm):
    select="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
    use_priceavg = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','placeholder':'ให้ระบบหารราคาให้'}), required=False,label='ให้เว็บหารราคาให้')
    apps = forms.ModelChoiceField(queryset=Apps.objects.filter(isApproved=True), widget=forms.Select(attrs={'placeholder':'เลือกแอปพลิเคชั่น','class':select}),label='เลือกแอปพลิเคชั่น')
    class Meta:
        select="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
        style='bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
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
            'title':forms.TextInput(attrs={'class':style,}),
            'quantity':forms.NumberInput(attrs={'class':style,}),
            'bank':forms.Select(attrs={'class':select}),
            'bankaccount':forms.TextInput(attrs={'class':style,}),
            'price':forms.NumberInput(attrs={'class':style,'placeholder':'ราคา'}),
            'priceaverage':forms.NumberInput(attrs={'class':style,'placeholder':'ราคาเฉลี่ย'}),
            'paid_day':forms.NumberInput(attrs={'class':style,'placeholder':'จ่ายทุกวันที่'}),
            'qrcodeImage':forms.FileInput(attrs={'class':"block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400",}),

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

