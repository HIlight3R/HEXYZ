from django.shortcuts import render
from django.views.generic.base import View

from .models import Wallet


class WalletsView(View):
    """Wallet view class"""

    def get(self, request):
        wallets = Wallet.objects.all()
        return render(request, "coins/wallets.html", {"wallet_list": wallets})
