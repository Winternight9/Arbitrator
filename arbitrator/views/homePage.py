import sys

from django.shortcuts import render


def homePage(request):
    return render(request, 'arbitrator/testhome.html')

sys.modules[__name__] = homePage    