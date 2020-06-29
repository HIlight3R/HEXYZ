def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a matching profile."""

    from .models import Wallet

    if created:
        Wallet(user=instance).save()
