import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ArbitratorUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', blank=True, null=True)


    def __str__(self):
        return self.user.username


class Polls(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    polls_text = models.CharField(max_length = 100)
    created = models.DateTimeField('created date', auto_now_add=True)


    def __str__(self):
        return self.pollname

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    polls = models.ForeignKey(Polls, on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('Date Published',auto_now=True)


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chocie_text = models.CharField(max_length = 100)

    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    polls = models.ForeignKey(Polls, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_date = models.DateTimeField('Voted Date',max_length = 100, auto_now=True)

