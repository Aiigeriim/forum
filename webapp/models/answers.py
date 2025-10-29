from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel, Topic


class Answer(BaseCreateUpdateModel):
    answer = models.TextField(verbose_name='Ответ')
    topic = models.ForeignKey('webapp.Topic', on_delete=models.CASCADE, related_name='answers',verbose_name='Тема')

    class Meta:
        db_table = 'answers'
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


    def __str__(self):
        return self.answer

    def get_absolute_url(self):
        return reverse('webapp:topic_view', kwargs={'pk': self.topic_id})