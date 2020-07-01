from django.db.models import Sum
from django.shortcuts import render
from django.views.generic.base import View

from .models import Wallet


class WalletsView(View):
    """Wallet view class"""

    def get(self, request):
        wallets = Wallet.objects.all()
        totals = wallets.aggregate(Sum('balance'))
        total = totals.get('balance__sum')
        return render(request, "coins/wallets.html", {"wallet_list": wallets, "total_sum": total})
