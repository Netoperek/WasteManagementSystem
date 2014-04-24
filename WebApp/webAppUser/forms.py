from django import forms
from webAppUser.models import WebAppUser
from django.contrib.auth.models import User

class WebAppUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')