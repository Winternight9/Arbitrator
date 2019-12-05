from django.contrib import admin
from arbitrator.models import ArbitratorUser
from arbitrator.models import Poll
from arbitrator.models import Question
from arbitrator.models import Choice
from arbitrator.models import Vote
from arbitrator.models import ChoiceAnswer
from arbitrator.models import TextAnswer
from arbitrator.models import PollSubmission

admin.site.register(ArbitratorUser)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(ChoiceAnswer)
admin.site.register(TextAnswer)
admin.site.register(PollSubmission)
