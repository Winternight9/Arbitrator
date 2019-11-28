import sys


from django import forms
from django.utils.safestring import mark_safe
from arbitrator.models import Poll


class PollForm(forms.Form):
    def __init__(self, poll_id, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.poll =  Poll.objects.get(id=poll_id)
        self.questions = self.poll.questions_set.values()

sys.module[__name__] = PollForm