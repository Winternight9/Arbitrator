import sys

from django.shortcuts import render, reverse, redirect
from arbitrator.forms import LoginForm


def indexView(request):
    form = LoginForm()
    context = {
        'form':  form
    }
    if request.user.is_authenticated:
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:    
            return redirect(reverse("arbitrator:home"))
    else:
        return render(request, 'arbitrator/index.html', context, status=200)


sys.modules[__name__] = indexView
