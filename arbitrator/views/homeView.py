import sys

from django.shortcuts import render, reverse, redirect
from arbitrator.models import Poll
from arbitrator.models import PollSubmission


def home(request):
    polls = Poll.objects.all().order_by('-is_vote_available', '-pollsubmission',)

    voted_poll_ids = [
        submission.poll_id
        for submission in PollSubmission.objects.filter(
            user_id=request.user.id
        )
    ]

    context = {
        "polls": polls,
        "voted_poll_ids": voted_poll_ids
    }

    return render(request, 'arbitrator/home.html', context)


sys.modules[__name__] = home
