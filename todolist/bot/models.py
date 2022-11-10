from django.db import models
from core.models import User
import random

CODE_VACABULARY = 'qwertyuiopasdfghjklzxcvbnm123456789'


class TgUser(models.Model):
    class Meta:
        verbose_name = 'tg пользователь'
        verbose_name_plural = 'tg пользователи'
        
    tg_chat_id = models.BigIntegerField(
        verbose_name='Chat ID', unique=True,
    )
    tg_id = models.BigIntegerField(
          verbose_name='Telegramm ID', unique=True,
    )
    username = models.CharField(
        verbose_name='Telegramm Username', max_length=255, null=True, blank=True, default=None,
    )
    verification_code = models.CharField(
        verbose_name='Code accept', max_length=32,
    )
    user = models.ForeignKey(
        User,
        models.PROTECT,
        null=True,
        blank=True,
        default=None,
        verbose_name='Связанный пользователь'
    )
    
    def set_verification_code(self):
        'random choices code'
        code = "".join([random.choice(CODE_VACABULARY) for _ in range(12)])
        self.verification_code = code


