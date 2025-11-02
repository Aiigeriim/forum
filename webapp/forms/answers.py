from django.forms import CharField, TextInput

from webapp.forms import BaseForm
from webapp.models import Answer


class AnswerForm(BaseForm):
    answer = CharField(widget=TextInput(attrs={'class': 'form-control'}), required=False, label='Ваш комментарий')

    class Meta:
        model = Answer
        fields = ['answer',]