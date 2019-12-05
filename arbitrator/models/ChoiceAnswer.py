import sys

from django.db import models
from arbitrator.models import Choice
from arbitrator.models import PollSubmission


class ChoiceAnswer(models.Model):
    poll_submission = models.ForeignKey(PollSubmission, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = ChoiceAnswer
