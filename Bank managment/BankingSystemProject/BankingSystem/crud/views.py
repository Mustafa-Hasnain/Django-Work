from unicodedata import name
from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .form import cus,acc, Withdraw, Transfer
from .models import Account, Customer
from django.contrib import messages

from crud import form
# Create your views here.

def index(request):
    return render(request, 'crud/index.html')

def addCustomer(request,id=0):
    if request.method == 'GET': # if land by clicking add button
        if id==0:
            form = cus()
            return render(request, 'crud/addCustomer.html', {'form':form})
        # else: # from update link
        #     customers = Customer.objects.get(pk=id)
        #     form = cus(instance=customers)
        #     return render(request, 'crud/addCustomer.html', {'form': form})
    else : # when method == post
         if id == 0:
             form = cus(request.POST)
             if form.is_valid():
                 form.save()
             return redirect('../crud/addAccount')
    #     else: # for update in database
    #         customers = Customer.objects.get(pk=id)
    #         form = cus(request.POST, instance=customers)
    #         if form.is_valid():
    #             form.save()
    #         return redirect('../show')


    #
def addAccount(request,id=0):
    if request.method == 'GET':  # if land by clicking add button
        if id == 0:
            form = acc()
            return render(request, 'crud/addAccount.html', {'form':form})
    else :
         if id == 0:
             form = acc(request.POST)
             if form.is_valid():
                 form.save()
             return redirect('../crud/show')

def show(request):
    if request.method == 'GET':
        customer_list = Customer.objects.all().order_by('customer_name')
        account_list = Account.objects.all()

    else:
        customer_list = Customer.objects.filter(customer_name__startswith = request.POST['text'] )
    return render(request, 'crud/show.html', {'customer_list': customer_list ,'account_list': account_list})


def depositMoney(request):
    return render(request,'crud/deposit.html')

def deposit(request):
    if request.method == 'POST':
        account_no = request.POST['acc_no']
        amount = int(request.POST['amount'])
        table = Account.objects.get(account_num = account_no)
        table.balance += amount
        table.save()
        return redirect('show')
    else:
        return render(request, 'crud/deposit.html')

    #else:
       # form = acc()
        #return render(request, 'crud/deposit.html', {'form': form})

def transfer(request):
    return render(request, 'crud/transfer.html')

def TransferMoney(request):
    form = Transfer(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            acc_no1 = form.cleaned_data['acc_no1']
            acc_no2 = form.cleaned_data['acc_no2']
            amount = form.cleaned_data['amount']
            payer1 = Account.objects.get(account_num=acc_no1)
            payer2 = Account.objects.get(account_num=acc_no2)

            payer1.balance -= amount
            payer1.save()

            payer2.balance += amount
            payer2.save()
            return redirect('show')
        else:
            form = Transfer()
    return render(request, 'crud/transfer.html', {'form':form})



def withdraw(request):
    return render(request, 'crud/withdraw.html')

def WithDraw(request):
    form = Withdraw(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            acc_no = form.cleaned_data['acc_no']
            amount = form.cleaned_data['amount']
            table = Account.objects.get(account_num = acc_no)
            table.balance -= amount
            table.save()
            return redirect('show')
        else:
            form = Withdraw()
    return render(request, 'crud/withdraw.html', {'form':form})
