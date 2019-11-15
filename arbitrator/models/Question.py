import sys

from django.db import models
from arbitrator.models import Poll


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = Question
