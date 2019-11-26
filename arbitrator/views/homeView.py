import sys

from django.shortcuts import render, reverse, redirect
from arbitrator.models import Poll


def home(request):
    polls = Poll.objects.all()
    context = {
        "polls": polls
    }

    return render(request, 'arbitrator/home.html', context)


sys.modules[__name__] = home
