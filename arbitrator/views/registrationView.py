import sys

from django.shortcuts import render, reverse, redirect
from ..forms import RegistrationForm


def registrationView(request):
    form = RegistrationForm()
    context = {
        'form':  form
    }

    return render(request, 'arbitrator/registration.html', context)


sys.modules[__name__] = registrationView
