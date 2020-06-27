# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View

from coins.models import User


class UsersView(View):
    """Users' view class"""

    def get(self, request):
        users = User.objects.all()
        return render(request, "coins/users.html", {"user_list": users})
