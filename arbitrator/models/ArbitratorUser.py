import sys

from django.db import models
from django.contrib.auth.models import User


class ArbitratorUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.user

    class Meta:
        app_label = "arbitrator"


sys.modules[__name__] = ArbitratorUser
