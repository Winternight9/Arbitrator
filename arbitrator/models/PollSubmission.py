import sys

from django.db import models
from django.contrib.auth.models import User
from arbitrator.models import Poll


class PollSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    sub_date = models.DateTimeField('date submitted', auto_now=True)

    def __str__(self):
        return f"{poll} subbmitted by {user} on {sub_date}"

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = PollSubmission
