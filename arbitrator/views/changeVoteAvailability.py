import sys
import json

from django.shortcuts import render, reverse, redirect
from arbitrator.models import Poll
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



@login_required
def change_vote_availability(request):
	if request.method == "POST":
		poll_id = json.loads(request.body.decode("utf-8"))['pollID']

		poll = Poll.objects.get(id=poll_id)

		poll.change_vote_availability()

		return HttpResponse('ok', status=200)

	return HttpResponse('error', status=500)


sys.modules[__name__] = change_vote_availability
