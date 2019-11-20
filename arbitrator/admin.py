from django.contrib import admin
from arbitrator.models import ArbitratorUser, Poll, Question, Choice, Vote

admin.site.register(ArbitratorUser)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
