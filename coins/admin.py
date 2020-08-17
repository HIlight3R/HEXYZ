from django.contrib import admin

from .models import Wallet, Transfer, PromoCode


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "balance")
    list_display_links = ("id", "user")
    list_search = ("user", "id", "balance")
    list_editable = ("balance",)
    readonly_fields = ("user", "id")
    fieldsets = (
        (None, {
            "fields": (("id", "balance"), "user")
        }),
    )


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "amount", "datetime")
    list_display_links = ("sender", "receiver")
    list_search = ("sender", "receiver", "datetime")
    readonly_fields = ("sender", "receiver", "amount", "datetime")
    fieldsets = (
        (None, {
            "fields": (("sender", "receiver"), ("amount", "datetime"))
        }),
    )


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "amount", "is_applied")
    list_display_links = ("id", "key")
    list_editable = ("amount", "is_applied")
    list_search = ("id", "key")
    readonly_fields = ("id",)
    fieldsets = (
        (None, {
            "fields": (("key", "amount"), ("id", "is_applied"))
        }),
    )


admin.site.site_title = "АП HEXYZ"
admin.site.site_header = "Админ-панель HEXYZ"
