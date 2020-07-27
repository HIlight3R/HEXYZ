from django.contrib import admin

from .models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "balance")
    list_search = ("user", "id", "balance")
    list_editable = ("balance",)
    readonly_fields = ("user", "id")
    fieldsets = (
        (None, {
            "fields": (("id", "balance"), "user")
        }),
    )


admin.site.site_title = "АП HEXYZ"
admin.site.site_header = "HEXYZ"
