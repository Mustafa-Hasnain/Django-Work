from email import message
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.core.exceptions import ValidationError
from .form import sign_up, addproduct
from .models import Customer, Product
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = sign_up(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup SuccessFul")
        return redirect('/index/')
    else:
        form = sign_up()
        return render(request, 'signup.html', {'form':form})

def AddProduct(request):
    if request.method =='POST':
        form = addproduct(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "add product")
        return redirect('/addproduct/')
    else:
        form = addproduct()
        return render(request,'product.html', {'form':form}) 

def show(request):
    customer_lst = Customer.objects.all().order_by('id')
    return render(request, 'show.html', {'customer_lst':customer_lst})

def showproduct(request):
    pro_lst=Product.objects.all().order_by('id')
    return render(request,'showproduct.html',{'pro_lst':pro_lst})

def edit(request, id):
    if request.method == 'POST':
        customer_lst = Customer.objects.get(pk=id)
        form = sign_up(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/show/')
    else:
        customer_lst = Customer.objects.get(pk=id)
        form = sign_up(instance=customer_lst)
        return render(request, 'signup.html', {'form':form})
    
def delete(request, id):
    customer_lst = Customer.objects.get(pk=id)
    customer_lst.delete()
    return redirect('/show/')
