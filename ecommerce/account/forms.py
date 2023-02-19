from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
from django.forms.widgets import PasswordInput, TextInput
from django.template import RequestContext

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(CreateUserForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].required = True

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Ten email jest już zarejestrowany')
    #     return email
    
    #     if len(email >= 350):
    #         raise forms.ValidationError('Ten email jest za długi')
    #     return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class UpdateUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username']
        exclude = ['password1', 'password2']

















