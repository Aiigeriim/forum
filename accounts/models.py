from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class MyUser(AbstractUser):
    REQUIRED_FIELDS = [ 'password', 'avatar']
    avatar = models.ImageField(upload_to="avatars", verbose_name='Аватар')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # def get_absolute_url(self):
    #     return reverse("webapp:topics_list")
