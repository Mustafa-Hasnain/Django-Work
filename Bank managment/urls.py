from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addCustomer', views.addCustomer, name='addCustomer'),
    path('addAccount', views.addAccount, name='addAccount'),
    path('show', views.show, name='show'),
    path('deposit', views.deposit, name='deposit'),
    path('transfer', views.transfer, name='transfer'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('depositMoney', views.deposit, name='depositMoney'),
]
