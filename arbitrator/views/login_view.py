import sys

from django.shortcuts import render, reverse, redirect
from ..forms import RegistrationForm


def login_view(request):
    form = RegistrationForm()
    context = {
        'form':  form
    }

    return render(request, 'arbitrator/login.html', context)


sys.modules[__name__] = login_view
