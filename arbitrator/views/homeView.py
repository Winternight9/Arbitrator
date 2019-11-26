import sys

from django.shortcuts import render, reverse, redirect


def home(request):
    return render(request, 'arbitrator/home.html')


sys.modules[__name__] = home
