from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from webapp.forms import TopicForm
from webapp.models import Topic


class CreateTopic(LoginRequiredMixin, CreateView):
    form_class = TopicForm
    template_name = 'topics/create_topic.html'
    success_url = reverse_lazy('webapp:topics_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TopicsList(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'topics/topics_list.html'
    ordering = '-created_at'
    paginate_by = 2


class TopicDetail(DetailView):
    model = Topic
    template_name = 'topics/topic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answers"] = self.object.answers.order_by('created_at')
        return context




