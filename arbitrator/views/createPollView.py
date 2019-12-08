import sys
import json

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from arbitrator.models import Poll, Question, Choice, QuestionType, ArbitratorUser


@login_required
def createPollView(request):
    if request.method == "POST":
        try:
            savePoll(request)

            messages.success(
                request,
                "poll created"
            )
        except Exception as error:
            messages.error(
                request,
                "poll error please try again"
            )

        url = reverse('arbitrator:home')

        return HttpResponse(url)

    user = request.user
    context = {
        "user": user
    }

    return render(
        request,
        "arbitrator/createPoll.html",
        context
    )


def savePoll(request):
    poll_data = json.loads(request.body.decode("utf-8"))
    poll_label = poll_data['name']
    poll_questions = poll_data['questions']

    if poll_label == "":
        raise ValueError("PollNameIsNotValid")

    if not isinstance(poll_label, str):
        raise TypeError("PollNameTypeError")

    poll_db = Poll(
        owner=ArbitratorUser.objects.get(
            user=request.user),
        label=poll_label)

    poll_db.save()

    for question in poll_questions:
        question_label = question['label']
        question_type = QuestionType(question['type']).value

        if question_label == "":
            poll_db.delete()

            raise ValueError("QuestionNameIsNotValid")

        if not isinstance(question_label, str):
            poll_db.delete()

            raise TypeError("QuestionNameTypeError")

        if question_type not in [QuestionType.Text.value, QuestionType.Choice.value]:
            poll_db.delete()

            raise ValueError('QuestionTypeIsNotValid')

        question_db = Question(
            label=question_label,
            type=question_type,
            poll=poll_db,
        )

        question_db.save()

        if question_type == QuestionType.Choice.value:
            choices = question['choices']

            if choices == []:
                poll_db.delete()

                raise ValueError('ChoiceQuestionHasNoChoice')

            question_multiple_selection = bool(question['multipleSelection'])
            question_db.multiple_selection = multiple_selection = question_multiple_selection

            question_db.save()

            for choice in choices:
                choice_db = Choice(
                    label=choice,
                    question=question_db
                )

                choice_db.save()


sys.modules[__name__] = createPollView
