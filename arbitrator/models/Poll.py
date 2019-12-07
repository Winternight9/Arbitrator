import sys

from django.db import models
from arbitrator.models import ArbitratorUser


class Poll(models.Model):
    owner = models.ForeignKey(ArbitratorUser, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    is_vote_available = models.BooleanField(default=True)
    is_result_available = models.BooleanField(default=True)

    def __str__(self):
        return self.label

    def total_submission(self):
        return len(self.pollsubmission_set.values())

    def change_vote_availability(self):
        self.is_vote_available = not self.is_vote_available

        self.save()

    def change_result_availability(self):
        self.is_result_available = not self.is_result_available

        self.save()

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = Poll
