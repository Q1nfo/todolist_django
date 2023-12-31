from django.db import models

from core.models import User


class TgUser(models.Model):
    """Модель телеграмм юзера"""
    chat_id = models.BigIntegerField(verbose_name='CHAT ID', unique=True)
    username = models.CharField(verbose_name='Username', max_length=255, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    verification_code = models.CharField(max_length=32, null=True, blank=True, default=None)
