from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView

from webapp.forms import AnswerForm
from webapp.models import Answer, Topic


class AnswerAdd(CreateView):
    form_class = AnswerForm
    template_name = 'answers/answer_create.html'


    def form_valid(self, form, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        form.instance.topic = topic
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        context['topic'] = topic
        return context

class AnswersList(ListView):
    paginate_by = 3
    model = Answer
    context_object_name = 'answers'
    template_name = 'partial/answers_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer = get_object_or_404(Answer, pk=self.kwargs['pk'])
        context['topic'] = Topic.objects.get(pk=answer.topic.pk)
        return context