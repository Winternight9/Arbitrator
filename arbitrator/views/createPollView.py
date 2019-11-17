import sys

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required
def createPollView(request):
    user = request.user
    context = {user: user}

    return render(request, "arbitrator/createPoll.html", context)


sys.modules[__name__] = createPollView
