import sys

from django.shortcuts import render, reverse, redirect


def index_view(request):
    return render(request, 'arbitrator/index.html')


sys.modules[__name__] = index_view
