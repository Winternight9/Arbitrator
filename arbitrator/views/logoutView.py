import sys

from django.shortcuts import render, redirect
from django.contrib.auth import logout


def logoutView(request):
    logout(request)

    return redirect('arbitrator:home')


sys.modules[__name__] = logoutView
