import sys

from django.shortcuts import render, reverse, redirect


def test(request):
    return render(request, 'arbitrator/test.html')


sys.modules[__name__] = test
