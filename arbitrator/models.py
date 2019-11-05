import datetime
from django.db import models
from django.contrib.auth.models import User

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
