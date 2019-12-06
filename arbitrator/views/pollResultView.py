import sys
import json

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from arbitrator.models import Question
from arbitrator.models import QuestionType
from arbitrator.models import Poll
from arbitrator.models import Choice
from arbitrator.models import TextAnswer
from arbitrator.models import ChoiceAnswer


def pollResultView(request, poll_id):
    try:
        poll_name = Poll.objects.get(id=poll_id).label
        questions = Question.objects.filter(poll_id=poll_id)
        results = {
            'data': []
        }

        for question in questions:
            question_type = question.type

            if question_type == QuestionType.Text.value:
                results['data'].append(
                    {
                        'label': question.label,
                        'type': question_type,
                        'answers': [
                            answer["value"] for answer in question.textanswer_set.values()
                        ]
                    }
                )
            elif question_type == QuestionType.Choice.value:
                choices = Choice.objects.filter(question_id=question.id)

                results['data'].append(
                    {
                        'label': question.label,
                        'type': question_type,
                        'answers': [
                            {
                                'label': choice.label,
                                'voteCount': ChoiceAnswer.get_vote_count_by_choice_id(choice.id)
                            } for choice in choices
                        ]
                    }
                )

        results = json.dumps(results)

    except Exception as error:
        messages.error(request, "NoResult")

        return redirect(reverse("arbitrator:home"))

    context = {
        'poll_name': poll_name,
        'results': results,
    }

    return render(request, 'arbitrator/pollResult.html', context)


sys.modules[__name__] = pollResultView
