import sys
import enum


class QuestionType(enum):
    Text = 0
    Choice = 1


sys.modules[__name__] = QuestionType
