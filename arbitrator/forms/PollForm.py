import sys


from django import forms
from django.utils.safestring import mark_safe
from arbitrator.models import Poll
from arbitrator.models import Question
from arbitrator.models import QuestionType


class PollForm(forms.Form):
    def __init__(self, poll_id, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.poll = Poll.objects.get(id=poll_id)
        self.questions = Question.objects.filter(poll_id=poll_id)
        for question in self.questions:
            question_type = question.type

            if question_type == QuestionType.Text.value:
                self.fields[question.label] = forms.CharField(
                    min_length=1,
                    widget=forms.TextInput(
                        attrs={
                            'class': 'input',
                        }
                    ),
                    label=mark_safe(f"{question.label}</br>")
                )
            elif question_type == QuestionType.Choice.value:
                choices = question.choice_set.values()
                CHOICES = [
                    (str(choice["id"]), str(choice["label"]))
                    for choice in choices
                ]

                multiple_selection = question.multiple_selection

                if multiple_selection:
                    self.fields[question.label] = forms.MultipleChoiceField(
                        widget=forms.CheckboxSelectMultiple(
                            attrs={
                                'class': 'checkbox',
                            }
                        ),
                        choices=CHOICES,
                    )
                else:
                    self.fields[question.label] = forms.ChoiceField(
                        widget=forms.RadioSelect(
                            attrs={
                                'class': 'checkbox',
                            }
                        ),
                        choices=CHOICES
                    )


sys.modules[__name__] = PollForm
