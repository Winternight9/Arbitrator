import sys

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


sys.modules[__name__] = EditProfileForm
    