from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from webapp.forms import AnswerForm
from webapp.models import Answer, Topic


class AnswerAdd(LoginRequiredMixin, CreateView):
    form_class = AnswerForm
    template_name = 'answers/answer_create.html'


    def form_valid(self, form, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        form.instance.topic = topic
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        context['topic'] = topic
        return context


class AnswerUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'answers/answer_update.html'
    form_class = AnswerForm
    model = Answer
    permission_required = 'webapp.change_answer'


    def has_permission(self):
        answer = get_object_or_404(Answer, pk=self.kwargs['pk'])
        return super().has_permission() or answer.author == self.request.user


class AnswerDelete(PermissionRequiredMixin, DeleteView):
    model = Answer
    template_name = 'answers/answer_delete.html'
    permission_required = 'webapp.delete_answer'

    def has_permission(self):
        answer = get_object_or_404(Answer, pk=self.kwargs['pk'])
        return super().has_permission() or answer.author == self.request.user

    def get_success_url(self):
        return self.object.get_absolute_url()

