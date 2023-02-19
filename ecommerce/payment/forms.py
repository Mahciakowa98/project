from django import forms
from . models import ShippingAddress

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'address1', 'city', 'zipcode']
        exclude = ['user',]
