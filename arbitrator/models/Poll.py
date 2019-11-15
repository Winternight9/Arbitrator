import sys

from django.db import models
from arbitrator.models import ArbitratorUser


class Poll(models.Model):
    owner = models.ForeignKey(ArbitratorUser, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    created_date = models.DateTimeField('created date', auto_now_add=True)

    def __str__(self):
        return self.label

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = Poll
