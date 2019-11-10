import sys


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.safestring import mark_safe


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.CharField(
        max_length=14,
        min_length=1,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'id': 'username-field'
            }
        ),
        label=mark_safe("Username</br>"))

    password = forms.CharField(
        max_length=14,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'id': 'password-field'
            }),
        label=mark_safe("Password</br>"))


sys.modules[__name__] = LoginForm
