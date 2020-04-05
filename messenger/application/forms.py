from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(max_length=30, label='Login')
    password = forms.CharField(max_length=30, label='Password')
