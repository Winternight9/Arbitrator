import sys

from django.shortcuts import render, reverse, redirect
from ..forms import RegistrationForm


def registration_view(request):
    form = RegistrationForm()
    context = {
        'form':  form
    }

    return render(request, 'arbitrator/login.html', context)


sys.modules[__name__] = registration_view
