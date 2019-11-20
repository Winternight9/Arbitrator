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
        except:
            messages.error(
                request,
                "poll error please try again"
            )

        url = reverse('arbitrator:test')

        return HttpResponse(url)

    user = request.user
    context = {user: user}

    return render(
        request,
        "arbitrator/createPoll.html",
        context
    )


def savePoll(request):
    pollData = json.loads(request.body.decode("utf-8"))
    pollLabel = pollData['name']
    pollQuestions = pollData['questions']

    if pollLabel == "":
        raise ValueError("PollNameIsNotValid")

    if not isinstance(pollLabel, str):
        raise TypeError("PollNameTypeError")

    poll_db = Poll(
        owner=ArbitratorUser.objects.get(
            user=request.user),
        label=pollLabel)

    poll_db.save()

    for question in pollQuestions:
        question_label = question['label']
        question_type = QuestionType(question['type'])
        question_multiple_selection = bool(question['multipleSelection'])

        if question_type not in [QuestionType.Text, QuestionType.Choice]:
            raise ValueError('QuestionTypeIsNotValid')

        question_db = Question(
            label=question_label,
            type=question_type,
            poll=poll_db,
            multiple_selection=question_multiple_selection
        )

        question_db.save()

        if question_type == QuestionType.Choice:
            for choice in question['choices']:
                choice_db = Choice(
                    label=choice,
                    question=question_db
                )

                choice_db.save()


sys.modules[__name__] = createPollView
