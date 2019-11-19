import sys

from django.shortcuts import render, reverse, redirect
from arbitrator.forms import LoginForm


def indexView(request):
    form = LoginForm()
    context = {
        'form':  form 
    }
    if request.user.is_authenticated:
        return redirect(reverse("arbitrator:test"))
    else:
        return render(request, 'arbitrator/index.html', context, status=200)


sys.modules[__name__] = indexView
