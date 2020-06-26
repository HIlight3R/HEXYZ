from django.contrib import admin

from .models import User


@admin.register(User)
class CategoryUser(admin.ModelAdmin):
    list_display = ("login", "name", "balance")
    list_filter = ("login", "name", "balance")
    readonly_fields = ("password",)
    fieldsets = (
        ("Основная информация", {
            "fields": (("name", "balance"),)
        }),
        ("Данные для входа", {
            "fields": (("login", "password"),)
        })
    )


admin.site.site_title = "Администрирование HEXYZ"
admin.site.site_header = "Админ-панель HEXYZ"
