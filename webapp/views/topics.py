

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from webapp.forms import TopicForm, AnswerForm
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


class TopicDetail(DetailView, MultipleObjectMixin):
    model = Topic
    template_name = 'topics/topic_detail.html'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        object_list = topic.answers.all()
        answer_form = self.get_answer_form(self.request)
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['answer_form'] = answer_form['answer_form']
        return context

    def get_answer_form(self, request):
        return {'answer_form': AnswerForm(request.GET)}



class TopicUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'topics/topic_update.html'
    model = Topic
    form_class = TopicForm
    permission_required = 'webapp.change_topic'

    def has_permission(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return super().has_permission() or topic.author == self.request.user



class TopicDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'topics/topic_delete.html'
    model = Topic
    permission_required = 'webapp.delete_topic'
    success_url = reverse_lazy('webapp:topics_list')

    def has_permission(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return super().has_permission() or topic.author == self.request.user


