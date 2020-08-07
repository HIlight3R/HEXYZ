import random
import string

from django.contrib.auth.models import User
from django.db import models

from .signals import create_profile


class Wallet(models.Model):
    """Кошельки"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=False)
    balance = models.DecimalField("Баланс", max_digits=15, decimal_places=3, default=0, null=False)

    def __str__(self):
        return f"{self.user.username} (#{self.user.id})"

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"


models.signals.post_save.connect(create_profile, sender=User)


class Transfer(models.Model):
    """Переводы"""
    sender = models.ForeignKey(to=Wallet, verbose_name="Отправитель", on_delete=models.DO_NOTHING,
                               related_name="transfer_sender", null=False)
    receiver = models.ForeignKey(to=Wallet, verbose_name="Получатель", on_delete=models.DO_NOTHING,
                                 related_name="transfer_receiver", null=False)
    amount = models.DecimalField("Сумма", max_digits=15, decimal_places=3, default=0, null=False)
    datetime = models.DateTimeField("Дата и время", auto_now_add=True, null=False)

    def __str__(self):
        return f"{self.sender.user.username} (#{self.sender.id}) => {self.receiver.user.username} (#{self.receiver.id}) {self.amount} HEX"

    class Meta:
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"


class PromoCode(models.Model):
    """Промокоды"""
    amount = models.DecimalField("Сумма", max_digits=15, decimal_places=3, default=0, null=False)
    key = models.SlugField("Ключ", default=''.join(random.choices(string.ascii_uppercase + string.digits, k=16)),
                           null=False, unique=True)
    is_applied = models.BooleanField("Применен", default=False)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"
