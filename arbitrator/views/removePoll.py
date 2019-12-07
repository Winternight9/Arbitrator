import sys
import json

from arbitrator.models import Poll
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



@login_required
def remove_poll(request):
	if request.method == "POST":
		poll_id = json.loads(request.body.decode("utf-8"))['pollID']

		poll = Poll.objects.get(id=poll_id)

		poll.delete()

		return HttpResponse('ok', status=200)

	return HttpResponse('error', status=500)

sys.modules[__name__] = remove_poll
