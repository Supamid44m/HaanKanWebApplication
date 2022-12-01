from django import forms
from Party.models import Party

class cratePartyforms(forms.ModelForm):
    class Meta:
        model=Party
        fields=['title','apps','quantity','price']