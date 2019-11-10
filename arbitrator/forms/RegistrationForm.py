import sys

from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.CharField(
        max_length=14,
        min_length=6,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'id': 'username-field'
            }
        ),
        label=mark_safe("Username</br>"))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'id': 'email-field'
            }
        ),
        label=mark_safe("Email</br>"))

    password1 = forms.CharField(
        max_length=14,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'id': 'password-field'
            }),
        label=mark_safe("Password</br>"))

    password2 = forms.CharField(
        max_length=14,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'id': 'confirm-password-field'
            }),
        label=mark_safe("Confirm Password</br>"))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


sys.modules[__name__] = RegistrationForm
