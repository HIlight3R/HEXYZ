from django.db import models


class User(models.Model):
    """Class of user"""
    name = models.CharField("Имя", max_length=30)
    login = models.SlugField("Логин", max_length=64, unique=True)
    password = models.SlugField("Хэш пароля")
    balance = models.PositiveIntegerField("Баланс", default=0)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
