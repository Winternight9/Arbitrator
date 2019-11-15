import sys

from django.db import models
from arbitrator.models import ArbitratorUser, Choice


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    owner = models.ForeignKey(ArbitratorUser, on_delete=models.CASCADE)
    voted_date = models.DateTimeField(
        'voted date', max_length=100, auto_now=True)

    def __str__(self):
        return f"voted choice: {self.choice} by: {self.owner}"


sys.modules[__name__] = Vote
