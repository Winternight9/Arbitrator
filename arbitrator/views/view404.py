import sys

from django.shortcuts import render

def view404(request, *args, **kwargs):

    return render(request, 'arbitrator/404.html')



sys.modules[__name__] = view404