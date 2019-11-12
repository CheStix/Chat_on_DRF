from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User


class ChatRoom(models.Model):
    """Модель комнаты чата
    """
    creater = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Участники', related_name='invited_user')
    data = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Message(models.Model):
    """Модель сообщения
    """
    room = models.ForeignKey(ChatRoom, verbose_name='Комната', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    data = models.DateTimeField('Отправлено', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
