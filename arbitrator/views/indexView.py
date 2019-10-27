import sys

from django.shortcuts import render

def indexView(request):
    return render(request, 'arbitrator/index.html')

sys.modules[__name__] = indexView    
    
    
