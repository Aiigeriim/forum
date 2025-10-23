from django.db import models

from webapp.models import BaseCreateUpdateModel


class Topic(BaseCreateUpdateModel):
    topic = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Содержимое')

    class Meta:
        db_table = 'topics'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.topic

    # def get_absolute_url(self):
    #     return reverse('webapp:topic_detail', kwargs={'pk': self.pk})