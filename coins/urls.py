from django.urls import path

from . import views

urlpatterns = [
    path('', views.WalletsView.as_view(), name='wallets'),
    path('transfer/', views.TransferView.as_view(), name='transfer')
]
