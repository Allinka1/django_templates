from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=40, help_text='40 characters or fewer')
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            self.add_error(None, 'username exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        super(UserRegistrationForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            self.add_error(None, 'passwords does not match ')
            self.add_error(None, 'passwords does not match ')



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserChangePassword(forms.Form):
    old_password = forms.CharField(label='Current Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def clean(self):
        super(UserChangePassword, self).clean()
        old_password =self.cleaned_data.get('old_password') 
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if confirm_password != new_password:
            self.add_error(None, 'passwords does not match ')
            self.add_error(None, 'passwords does not match ')


class UserInterviewForm(forms.Form):

    GENDER_CHOICES = [
        [1, 'M'], [2, 'F']
    ]

    ENGLISH_LEVEL = [
        [1, 'A1'], [2, 'A2'], [3, 'A2`B1'], [4, 'B1'], [5, 'B2'],
        [6, 'C1'], [7, 'C2']
    ]

    name = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    age = forms.IntegerField()
    english = forms.ChoiceField(choices=ENGLISH_LEVEL)
