import sys

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    first_name = forms.CharField(
        max_length=32,
        min_length=1,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
            }
        ),
        label=mark_safe("Firstname</br>"))

    last_name = forms.CharField(
        max_length=32,
        min_length=1,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
            }
        ),
        label=mark_safe("Lastname</br>"))

    email = forms.EmailField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
            }
        ),
        label=mark_safe("Email</br>"))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


sys.modules[__name__] = EditProfileForm
