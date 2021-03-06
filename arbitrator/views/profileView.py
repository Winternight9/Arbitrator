import sys

from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required


@login_required
def profileView(request):
    return render(request,'arbitrator/profile.html')


sys.modules[__name__] = profileView
