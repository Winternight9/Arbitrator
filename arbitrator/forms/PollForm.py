import sys


from django import forms
from django.utils.safestring import mark_safe
from arbitrator.models import Poll
from arbitrator.models import Question
from arbitrator.models import QuestionType
from arbitrator.models import PollSubmission
from arbitrator.models import TextAnswer
from arbitrator.models import Choice
from arbitrator.models import ChoiceAnswer


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

    def save(self, user):
        poll_submission_db = PollSubmission(
            user=user,
            poll=self.poll
        )

        poll_submission_db.save()

        for question in self.questions:
            question_type = question.type

            if question_type == QuestionType.Text.value:
                text_answer_value = self.cleaned_data[question.label]

                text_answer_db = TextAnswer(
                    poll_submission=poll_submission_db,
                    value=text_answer_value,
                    question=question
                )

                text_answer_db.save()
            elif question_type == QuestionType.Choice.value:
                multiple_selection = question.multiple_selection

                if multiple_selection:
                    choice_ids = self.cleaned_data[question.label]

                    for choice_id in choice_ids:
                        choice = Choice.objects.get(id=choice_id)

                        choice_answer_db = ChoiceAnswer(
                            poll_submission=poll_submission_db,
                            choice=choice
                        )

                        choice_answer_db.save()
                else:
                    choice_id = self.cleaned_data[question.label]

                    choice = Choice.objects.get(id=choice_id)

                    choice_answer_db = ChoiceAnswer(
                        poll_submission=poll_submission_db,
                        choice=choice
                    )

                    choice_answer_db.save()


sys.modules[__name__] = PollForm
