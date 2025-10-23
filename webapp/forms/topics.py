from webapp.forms import BaseForm
from webapp.models import Topic


class TopicForm(BaseForm):
    class Meta:
        model = Topic
        fields = ['topic', 'content',]
