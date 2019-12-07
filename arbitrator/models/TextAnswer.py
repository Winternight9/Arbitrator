import sys

from django.db import models
from arbitrator.models import Question
from arbitrator.models import PollSubmission


class TextAnswer(models.Model):
    poll_submission = models.ForeignKey(PollSubmission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        app_label = "arbitrator"

    @staticmethod
    def get_text_answers_by_question_id(id):
        return TextAnswer.objects.filter(question_id=id)


sys.modules[__name__] = TextAnswer
