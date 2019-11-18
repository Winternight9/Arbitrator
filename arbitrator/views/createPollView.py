import sys
import json

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from arbitrator.models import Poll, Question


@login_required
def createPollView(request):
    if request.method == "POST":
        pollData = request.body.decode("utf-8")

        messages.success(request, f"poll created")

        url = reverse('arbitrator:test')

        return HttpResponse(url)

    user = request.user
    context = {user: user}

    return render(request, "arbitrator/createPoll.html", context)


sys.modules[__name__] = createPollView
