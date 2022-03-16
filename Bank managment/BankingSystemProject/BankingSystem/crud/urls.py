from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addCustomer', views.addCustomer, name='addCustomer'),
    path('addAccount', views.addAccount, name='addAccount'),
    path('show', views.show, name='show'),
    path('TransferMoney', views.TransferMoney, name='TransferMoney'),
    path('transfer', views.TransferMoney, name='transfer'),
    path('depositMoney', views.deposit, name='deposit'),
    path('deposit', views.depositMoney, name='depositMoney'),
    path('WithDraw', views.WithDraw, name='WithDraw'),
    path('withdraw', views.WithDraw, name='withdraw')
]
