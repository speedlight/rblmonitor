from django import forms
from .models import Rbllist

class AddrForm(forms.Form):
    address = forms.GenericIPAddressField(label='IPv4 or IPv6 Address ')

    def clean_address(self):
        address = self.cleaned_data['address'] 
        return address
