from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),label="Last Name")
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),label="Username")
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype Password'}),label="Password Confirmation")

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
