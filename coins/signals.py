def create_profile(sender, instance, signal, created, **kwargs):
    """Когда создан пользователь, привязываем к нему кошелек"""

    from .models import Wallet

    if created:
        Wallet(user=instance).save()
