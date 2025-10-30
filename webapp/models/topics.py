from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Topic(BaseCreateUpdateModel):
    topic = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Содержимое')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='topics',verbose_name='Автор')

    class Meta:
        db_table = 'topics'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('webapp:topic_view', kwargs={'pk': self.pk})