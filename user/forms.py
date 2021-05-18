from django import forms
from django.core.exceptions import ValidationError


class AuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
