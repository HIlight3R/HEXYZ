from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Wallet, Transfer


class WalletsView(View):
    """Список кошельков на главной"""

    def get(self, request):
        wallets = Wallet.objects.all()
        transfers = Transfer.objects.order_by("-id")
        totals = wallets.aggregate(Sum('balance'))
        total = totals.get('balance__sum')
        last = Wallet.objects.last()
        return render(request, "coins/wallets.html",
                      {"wallet_list": wallets, "total_sum": total, "last_wallet": last, "transfer_list": transfers})

    def post(self, request):
        sender = Wallet.objects.get(id=request.user.id)
        receiver = Wallet.objects.get(id=int(request.POST.get("id")))
        if sender is not None and receiver is not None and sender != receiver:
            if request.POST.get("amount", False):
                amount = float(request.POST.get("amount"))
                if amount <= float(sender.balance):
                    sb = float(sender.balance)
                    rb = float(receiver.balance)
                    sb -= amount
                    rb += amount
                    sender.balance = sb
                    receiver.balance = rb
                    sender.save()
                    receiver.save()
                    Transfer.objects.create(sender=sender, receiver=receiver, amount=amount)
                else:
                    return HttpResponse(status=400)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)
        return redirect('./')
