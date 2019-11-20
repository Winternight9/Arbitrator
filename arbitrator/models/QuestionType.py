import sys
from enum import Enum


class QuestionType(Enum):
    Text = 'text'
    Choice = 'choice'


sys.modules[__name__] = QuestionType
