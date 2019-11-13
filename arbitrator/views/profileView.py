import sys

from django.shortcuts import redirect,render


def profileView(request):
    return render(request,'arbitrator/profile.html')


sys.modules[__name__] = profileView
