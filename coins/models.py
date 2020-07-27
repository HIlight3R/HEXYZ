from django.contrib.auth.models import User
from django.db import models

from .signals import create_profile


class Wallet(models.Model):
    """Кошельки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0)

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"


models.signals.post_save.connect(create_profile, sender=User)


class Transfer(models.Model):
    """Переводы"""
    sender = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING, related_name="transfersender")
    receiver = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING, related_name="transferreceiver")
    amount = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"
