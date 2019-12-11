import sys

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from arbitrator.models import Poll
from arbitrator.forms import PollForm
from arbitrator.models import PollSubmission
from django.contrib.auth.decorators import login_required


@login_required
def pollView(request, poll_id):
    if PollSubmission.objects.filter(user_id=request.user.id, poll_id=poll_id).count() != 0:
        messages.error(request, "YouAreNotAllowedToViewThisPoll")

        return redirect("arbitrator:home")

    if request.method == "POST":
        form = PollForm(poll_id, request.POST)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, "SubmissionSuccess")

            return redirect("arbitrator:home")

        messages.error(request, "SubmissionError")
    try:
        vote_status = Poll.objects.get(id=poll_id).is_vote_available
        if vote_status == False:
            messages.error(request, "PollNotAvaliableRightNow")
            return redirect("arbitrator:home")
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
