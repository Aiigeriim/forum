from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from webapp.forms.topics import TopicForm
from webapp.models import Topic


class CreateTopic(CreateView):
    form_class = TopicForm
    template_name = 'topics/create_topic.html'
    success_url = reverse_lazy('webapp:topics_list')


class TopicsList(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'topics/topics_list.html'
    ordering = '-created_at'


class TopicDetail(DetailView):
    model = Topic
    template_name = 'topics/topic_detail.html'
    queryset = Topic.objects.all()



