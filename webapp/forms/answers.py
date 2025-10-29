from webapp.forms import BaseForm
from webapp.models import Answer


class AnswerForm(BaseForm):
    class Meta:
        model = Answer
        fields = ['answer',]