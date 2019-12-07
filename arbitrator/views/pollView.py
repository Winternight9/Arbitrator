import sys

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from arbitrator.models import Poll
from arbitrator.forms import PollForm


def pollView(request, poll_id):
    if request.method == "POST":
        form = PollForm(poll_id, request.POST)

        if form.is_valid():
            form.save(request.user)
            messages.success(request, "SubmissionSuccess")

            return redirect("arbitrator:home")

        messages.error(request, "SubmissionError")
    try:
        poll_name = Poll.objects.get(id=poll_id).label
        form = PollForm(poll_id)
    except Exception as error:
        messages.error(request, "PollError")

        return redirect("arbitrator:home")

    context = {
        'poll_name': poll_name,
        'form': form
    }

    return render(request, 'arbitrator/poll.html', context)


sys.modules[__name__] = pollView
