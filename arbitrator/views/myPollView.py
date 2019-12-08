import sys

from django.shortcuts import render, reverse, redirect
from arbitrator.models import Poll
from django.contrib.auth.decorators import login_required
from arbitrator.models import ArbitratorUser


@login_required
def myPollView(request):
    polls = Poll.objects.filter(owner_id=ArbitratorUser.objects.get(user_id=request.user.id).id)
    context = {
        "polls": polls,
    }

    return render(request, 'arbitrator/myPoll.html', context)


sys.modules[__name__] = myPollView
