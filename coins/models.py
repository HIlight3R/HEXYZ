from django.contrib.auth.models import User
from django.db import models

from .signals import create_profile


class Wallet(models.Model):
    """Class of user in database"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0)


models.signals.post_save.connect(create_profile, sender=User)
