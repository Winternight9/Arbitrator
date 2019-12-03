import sys

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from arbitrator.models import Poll
from arbitrator.forms import PollForm


def pollView(request, poll_id):
    try:
        poll_name = Poll.objects.get(id=poll_id).label
        form = PollForm(poll_id)
    except Exception as error:
        print(error)
        messages.error(request, "PollError")
        return redirect("arbitrator:home")

    context = {
        'poll_name': poll_name,
        'form': form
    }

    return render(request, 'arbitrator/poll.html', context)


sys.modules[__name__] = pollView
