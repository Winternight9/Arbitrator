import sys

from django.db import models
from arbitrator.models import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.label} vote: {self.vote_count}"

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = Choice
